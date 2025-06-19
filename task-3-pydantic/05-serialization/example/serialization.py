
from pydantic import BaseModel , ConfigDict
from typing import List
from datetime import datetime


class User(BaseModel):
    id:int
    name:str
    email:str
    created_at:datetime
    address:str
    tags: List[str] = []
    model_config = ConfigDict(
        json_encoders={datetime:lambda v : v.strftime('%d-%m-%Y %H:%M:%S')}
     
    )

class Post(BaseModel):
    id:int
    title:str
    content:str
    author_id:int
    created_at:datetime

class Comment(BaseModel):
    id:int
    content:str
    author_id:int
    post_id:int
    created_at:datetime

# create a user instance

user = User(
    id=1,
    name="javed",
    email="javed@gmail.com",
    created_at=datetime.now(),
    address="123 main st",
    tags=["python", "developer"]
)

# Using Model_dump() to convert the user instance to a dictionary

# developer_dict = user.model_dump()
# print(developer_dict)

# Using Model_dump.json() to convert the user instance to a json string

print("================================================\n")

developer_json = user.model_dump_json()
print(developer_json)


print("==========================================================\n")