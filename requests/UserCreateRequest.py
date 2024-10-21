from pydantic import BaseModel
from datetime import date
from entity.relationship import Relationship

class UserCreateRequest(BaseModel):
    name: str
    birthday: date
    address: str
    cpf: int
    relationship: Relationship
