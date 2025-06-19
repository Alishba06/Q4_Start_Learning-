from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Cloth(BaseModel):
    name: str
    cloth_type : str
    size: str
    color: str
    price: float

cloths: List[Cloth] = []


@app.get("/")

def rea_root():
    return{"message" : "Welcome to Cloth Shope"}


@app.get("/cloths")

def get_cloths():
    return cloths


@app.post("/cloths")

def add_cloth(cloth: Cloth):
    cloths.append(cloth)
    return cloth

@app.put("/cloths/{cloth_id}")

def update_cloth(cloth_id: int , update_cloth: Cloth):
    for index , Cloth in enumerate(cloths):
        if Cloth.id == cloth_id:
            cloths[index] = update_cloth
            return update_cloth
    
    return {"error" : "Cloth not found"}