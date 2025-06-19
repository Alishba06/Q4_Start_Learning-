
from typing import List , Optional

from pydantic import BaseModel

class Address(BaseModel):
    steet:str
    city:str
    postal_code:int


class User(BaseModel):
    id:int
    name:str
    address:Address

class Comment(BaseModel):
    id: int
    content:str
    replies: Optional[List['Comment ']] = None

Comment.model_rebuild()

address = Address(
    steet=123,
    city="TandoAllahyar",
    postal_code="10001",
)


user = User(
    id=1,
    name="Basit",
    address= address,
)

Comment = Comment(
    id=1,
    content="First Comment",
    replies=[
        Comment(id=2,content="seconed comment")
    ]
)