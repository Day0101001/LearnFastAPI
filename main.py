from fastapi import FastAPI, HTTPException 
from models import Todo, TodoIn_Pydantic, Todo_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from pydantic import BaseModel

class Message(BaseModel):
    message: str
    
app = FastAPI()

@app.post("/todo", response_model=Todo_Pydantic)
async def create(todo:TodoIn_Pydantic):
    obj = await Todo.create(**todo.dict(exclude_unset=True))
    return await Todo.Todo_Pydantic

@app.get("/gettodo/{id}", response_model=TodoIn_Pydantic, responses={404:{"model":HTTPNotFoundError}})
async def get_one(id: int):
    return await TodoIn_Pydantic.from_queryset_single(Todo.get(id=id))

register_tortoise(
    app, 
    db_url="sqlite://store.db",
    modules={'models':['models']},
    generate_schemas=True,
    add_exception_handlers=True
    )