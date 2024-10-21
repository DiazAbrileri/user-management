from datetime import date
from entity.relationship import Relationship

class Pessoa:
    def __init__(self, name: str, birthday: date, address: str, cpf: int, relationship: Relationship):
        self.name = name
        self.birthday = birthday
        self.address = address
        self.cpf = cpf
        self.relationship = relationship