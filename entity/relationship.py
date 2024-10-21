from enum import Enum

class Relationship(str, Enum):
    solteiro = "Solteiro"
    casado = "Casado"
    divorciado = "Divorciado"
    viuvo = "Viuvo"
    separado = "Separado"
    outro = "Não Informado"
    
    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.lower() == value:
                return member
        return None