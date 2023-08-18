from flask import Flask, jsonify, request
from flask.views import MethodView

from models import Session, Declaration
from schema import UpdateDeclaration

app = Flask("app")


class DeclarationView(MethodView):
    def get(self, declaration_id: int):
        with Session() as session:
            declaration = session.get(Declaration, declaration_id)
            return jsonify(
                {"id": declaration.id, "name": declaration.owner})

    def post(self):
        with Session() as session:
            declaration = Declaration(**request.json)
            session.add(declaration)
            session.commit()
            return jsonify({"status": "success", "id": declaration.id})

    def delete(self, declaration_id):
        with Session() as session:
            user = session.get(Declaration, declaration_id)
            session.delete(user)
            session.commit()
            return jsonify({"status": "success", "id": declaration_id})


declaration_view = DeclarationView.as_view("declarations")
app.add_url_rule(
    "/declarations/<int:declaration_id>", view_func=declaration_view, methods=["GET", "DELETE"]
)
app.add_url_rule("/declarations/", view_func=declaration_view, methods=["POST"])
if __name__ == "__main__":
    app.run()
