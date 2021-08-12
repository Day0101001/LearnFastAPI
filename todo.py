from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI(title="TO DO API", version="V1")

BD_Todo=[]

class Todo(BaseModel):
    tache : str
    date_heure : str
    description : str

@app.get("/")
async def get_root():
    return {"TODO list"}

@app.get("/alltodo/", response_model=List[Todo])
async def get_all_todo():
    return BD_Todo

@app.get("/todo/{id}")
async def get_todo(id:int):
    try:
         return BD_Todo[id]
    except:
        raise HTTPException(status_code=404, detail="Todo n'existe pas")

@app.put("/todo/{id}")
async def update_todo(id:int, new_todo:Todo):
    try:
         BD_Todo[id]=new_todo
         return BD_Todo[id]
    except:
        raise HTTPException(status_code=404, detail="Todo n'existe pas")

@app.delete("/todo/{id}")
async def delete_todo(id:int):
    try:
         ojb = BD_Todo[id]
         print(id," ",ojb)
         BD_Todo.pop(id)
         return ojb
    except:
        raise HTTPException(status_code=404, detail="Todo n'existe")

@app.post("/todo/")
async def creat_todo(todo: Todo):
    BD_Todo.append(todo)
    return todo
    
    