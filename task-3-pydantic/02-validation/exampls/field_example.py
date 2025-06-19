from pydantic import BaseModel # type ignore
from typing import List 

class OrderItem(BaseModel):
    product_id: int
    name:str
    quantity:int
    price:float


class BlogPost(BaseModel):
    id:int
    title:str
    contect:str
    author:str
    tags:List[str]

