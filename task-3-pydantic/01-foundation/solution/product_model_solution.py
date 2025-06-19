
from pydantic import BaseModel


# Clothing Product Model with  id ,  name , category , color price , in_stock 

class Cloth(BaseModel):
    id:int
    name:str
    category:str
    siz: list[str]
    color: list[str]
    price:float
    in_stock:bool
    






