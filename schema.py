from typing import Optional

from pydantic import BaseModel


class UpdateDeclaration(BaseModel):
    header: Optional[str]
    description: Optional[str]
    owner: Optional[str]
    creation_time: Optional[str]
