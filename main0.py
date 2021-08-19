from fastapi import FastAPI, Form, Query, File, UploadFile
from typing import Optional, List
from pydantic import BaseModel
from enum import Enum
import os

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

@app.get("/items/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    os.mkdir('livres')
    
    return {"filename": file.filename}