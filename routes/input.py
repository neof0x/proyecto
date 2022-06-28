from modulefinder import packagePathMap
from fastapi import APIRouter, Response, Depends, HTTPException, status
from starlette.status import HTTP_201_CREATED
from schemas.input_schema import InputSchema
from config.db import engine
from models.input import inputs
from typing import List
import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

input_router = APIRouter()
security = HTTPBasic()

class InputCreationRequest(BaseModel):
    field_1: str
    author: str
    description: str
    my_numeric_field: float
    

memory_db=[]

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "german")
    correct_password = secrets.compare_digest(credentials.password, "123456")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user or password",
            headers={"WWW-Authenticate": "Basic"},            
        )
    return credentials.username


@input_router.get("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}


# @input_router.get("/api/input", response_model=List[InputCreationRequest])
# def get_input():
#     with engine.connect() as conn:
#         result = conn.execute(inputs.select()).fetchall()
#         return result


@input_router.get("/data/{input_id}", response_model=InputCreationRequest)
def get_inputs(input_id: str):
    with engine.connect() as conn:
        result = conn.execute(inputs.select().where(inputs.c.id == input_id)).first()

        return result


@input_router.post("/input/field_1", status_code=HTTP_201_CREATED)
def save_input_field_1(request: InputCreationRequest):
    with engine.connect() as conn:
        new_input = []
        new_input.append("")
        for a in request:
            if a[1] == request.field_1:
                F = request.field_1.upper()
                new_input.append(F)
            else:
                new_input.append(a[1])                  
        conn.execute(inputs.insert().values(new_input)) 
        return Response(status_code=HTTP_201_CREATED)

@input_router.post("/input/author", status_code=HTTP_201_CREATED)
def save_input_author(request: InputCreationRequest):
    with engine.connect() as conn:
        new_input = []
        new_input.append("")
        for a in request:
            if a[1] == request.author:
                F = request.author.upper()
                new_input.append(F)
            else:
                new_input.append(a[1])                   
        conn.execute(inputs.insert().values(new_input)) 
        return Response(status_code=HTTP_201_CREATED)

@input_router.post("/input/description", status_code=HTTP_201_CREATED)
def save_input_description(request: InputCreationRequest):
    with engine.connect() as conn:
        new_input = []
        new_input.append("")
        for a in request:
            if a[1] == request.description:
                F = request.description.upper()
                new_input.append(F)
            else:
                new_input.append(a[1])                  
        conn.execute(inputs.insert().values(new_input))  
        return Response(status_code=HTTP_201_CREATED)


@input_router.post("/input/my_numeric_field", status_code=HTTP_201_CREATED)
def save_input_my_numeric_field():    
    return {"error": "my_numeric_field no es un campo valido para convertir a mayuscula"}

@input_router.post("/input/random_field", status_code=HTTP_201_CREATED)
def save_input_random_field():    
    return {"error": "random_field no es un campo valido para convertir a mayuscula"}
