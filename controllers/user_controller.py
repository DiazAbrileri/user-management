from entity.relationship import Relationship
from entity.pessoa import Pessoa
from datetime import date
from fastapi import HTTPException
from entity import model
from database import SessionLocal
from faker import Faker
from random import randint, choice

db = SessionLocal()

def user_create(user: Pessoa):
    
    data_validate(user)
    
    person = model.Pessoa()
    person.name = user.name
    person.address = user.address
    person.birthday = user.birthday
    person.cpf = user.cpf
    person.relationship = user.relationship
    
    db.add(person)
    db.commit()
    return user

def user_update(user_id: int, newUserInfo: Pessoa):
    user = db.query(model.Pessoa).filter(model.Pessoa.cpf == user_id).first()
    if(user is None): # Search with CPF
        user = db.query(model.Pessoa).filter(model.Pessoa.id == user_id).first() # Search with Id
        if(user is None):
            raise HTTPException(status_code=404, detail="Usuario não encontrado no banco")
    
    user_id = user.id
    
    data_validate(newUserInfo)
    
    result = {"Cadastro Antigo": {
        "cpf": user.cpf,
        "birthday": user.birthday,
        "address": user.address,
        "name": user.name,
        "relationship": user.relationship
    }}
    
    user.cpf = newUserInfo.cpf
    user.birthday = newUserInfo.birthday
    user.address = newUserInfo.address
    user.name = newUserInfo.name
    user.relationship = newUserInfo.relationship
    db.commit()
    result["Cadastro Atualizado"] = {
        "cpf": user.cpf,
        "birthday": user.birthday,
        "address": user.address,
        "name": user.name,
        "relationship": user.relationship
    }
    
    result["result"] = "Cadastro Atualizado com sucesso"
    
    return result

def user_list():
    personList = db.query(model.Pessoa).all()
    if(len(personList) == 0):
        return {"Message":"Nenhum cadastro encontrado na Base", "Pessoa":personList}
    return {"Message":"Cadastros armazenados","Pessoa":personList}


def data_validate(user:Pessoa):
    if(user.name is None or user.name ==""):
        raise HTTPException(status_code=400, detail="Nome invalido")
    
    if(user.cpf is None or user.cpf == "" or len(str(user.cpf)) != 11):
        raise HTTPException(status_code=400, detail="Cpf invalido")
    else:
        oldUser = db.query(model.Pessoa).filter(model.Pessoa.cpf == user.cpf).first()
        print(oldUser)
        if (oldUser is not None):
            raise HTTPException(status_code=400, detail="Cpf já cadastrado na base")
        
        
    if(user.birthday is None or user.birthday > date.today()):
        raise HTTPException(status_code=400, detail="Data de nascimento invalida")
    
    if(user.address is None or user.address == ""):
        raise HTTPException(status_code=400, detail="Endereço não preenchido ou faltante")
    
    if(user.relationship is None or user.relationship == ""):
        user.relationship = "Outro" 
    

def user_delete(user_id: int):
    userToDelete = db.query(model.Pessoa).filter(model.Pessoa.id == user_id).first()
    if userToDelete is None:
        userToDelete = db.query(model.Pessoa).filter(model.Pessoa.cpf == user_id).first()
        
        if userToDelete is None:
            raise HTTPException(status_code=404, detail="Usuario não encontrado")
    result = {
        "result": "Usuario removido da Base",
        "User": {
            "Id": userToDelete.id,
            "Name": userToDelete.name
        }
    }
    db.delete(userToDelete)
    db.commit()
    return result

def user_test(times: int):
    result = {"Usuarios criados": []}
    fake = Faker()
    
    for _ in range(times):
        new_user = Pessoa(
            name=fake.name(),
            birthday=fake.date_of_birth(),
            address=fake.address(),
            cpf=randint(10000000000, 99999999999),
            relationship=choice([
                Relationship.solteiro,
                Relationship.casado,
                Relationship.divorciado,
                Relationship.viuvo,
                Relationship.outro
            ])
        )
        
        result["Usuarios criados"].append(user_create(new_user))
    
    return result