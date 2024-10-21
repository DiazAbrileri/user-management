from sqlalchemy import Column, Integer, String, Date,Enum
from database import Base
from entity.relationship import Relationship

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    birthday = Column(Date)
    address = Column(String)
    cpf = Column(Integer)
    relationship = Column(Enum(Relationship))