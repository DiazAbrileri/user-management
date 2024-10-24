﻿# User-management

An application to create an manage users, it works by API calls where every endpoint does something different

It was created using Python FastAPI and SQLAlchemy

## Installation

Installers used in this Repo

```bash
pip install faker
pip install fastapi
pip install uvicorn
pip install sqlalchemy
```

## Usage

To Start the application you should run it by typing this in the terminal
```bash
uvicorn main:app --reload
```

There is currently 5 endpoints pointed at the database

The first is the "/users/create", it lets you create users based on simple data
```curl
curl --request POST --url http://127.0.0.1:8000/users/create \
```
```json
{
    "name": "Helena Lanzo",
    "birthday": "2000-10-19",
    "address": "Avenia Paulista 1080",
    "cpf": 29865359090,
    "relationship": "Divorciado"
}
```

The second is the "/users/update/{id_user}", it let you update any value of an already existing user, you can just use the user cpf or the user id in the {id_user}
```curl
curl --request POST --url http://127.0.0.1:8000/users/update/{id_user}
```
```json
{
    "name": "Mc Lovin",
    "birthday": "1981-06-03",
    "address": "Momona Street 892",
    "cpf": 26879922082,
    "relationship": "Casado"
}
```

The third one is "/users/list", list all users stored in the database, it show its data like id, name, birthday etc..
``` curl
curl --request GET --url  http://127.0.0.1:8000/users/list
```

The fourth one is "/users/delete/{id_user}", like the name says it delete an user from the database, in case needed or just to prank someone, it also uses the user cpf or user id in the {id_user}
``` curl
curl --request delete --url http://127.0.0.1:8000/users/delete/{id_user}
```

The last one is "/users/test/{times}", it creates random users in the database so you can try it out or just to fill in the gap, {times} refers to how many users you want to create
```curl
curl --request GET --url http://127.0.0.1:8000//users/test/{times}
```
