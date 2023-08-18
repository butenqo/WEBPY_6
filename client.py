import requests


response = requests.post(
     "http://127.0.0.1:5000/declarations", json={"owner": "user_1", "header": 'TEST', "description": "test_1" }
)
response = requests.patch(
    "http://127.0.0.1:5000/declarations/3", json={"owner": "new_name"}
)
response = requests.delete(
"http://127.0.0.1:5000/declarations/1"
)
response = requests.get(
    "http://127.0.0.1:5000/declarations/5"
)
