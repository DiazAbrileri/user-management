from fastapi import FastAPI, Depends
from controllers.user_controller import  user_create, user_update,user_list,user_delete, user_test
from requests.UserCreateRequest import UserCreateRequest
from entity import model
from database import engine,SessionLocal
from entity.pessoa import Pessoa

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#Create User
@app.post("/users/create")
def userCreate(request: UserCreateRequest):
    newuser = user_create(Pessoa(request.name,
       request.birthday,
       request.address,
       request.cpf,
       request.relationship)
    )
    return newuser

#Update a user using the same request as last time
@app.post("/users/update/{id_user}")
def userUpdate(id_user: int,request: UserCreateRequest):
    updatedUser = user_update( id_user,Pessoa(request.name,
       request.birthday,
       request.address,
       request.cpf,
       request.relationship))
    return updatedUser

#List all users
@app.get("/users/list")
def userList():
    result = user_list()
    return result

#Delete user by id or CPF
@app.delete("/users/delete/{id_user}")
def userDelete(id_user: int):
    result = user_delete(id_user)
    return result

#Create users randommly
@app.get("/users/test/{times}")
def userTest(times: int):
    result = user_test(times)
    return result