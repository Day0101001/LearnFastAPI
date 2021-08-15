from fastapi import FastAPI, Form
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class CoordIn(BaseModel):
    password :str
    lat : float
    lon : float
    zoom : Optional[int]=None
    description : Optional[str]

class CoordOut(BaseModel):
    lat : float
    lon : float
    zoom : Optional[int]=None
    description : Optional[str]

@app.post("/position/", response_model=CoordOut)
async def make_position(coord: CoordIn):
    return coord


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/login/")
async def login(user:str=Form(...), password:str=Form(...)):
    return {user: user}

# @app.get("/component/{component_id}")
# async def get_component(component_id:int):
#     return {"component" : component_id} 

# @app.get("/component/")
# async def read_component(number:int, text:Optional[str]):
#     return {"number" : number, "text" : text}

    