
from pydantic import BaseModel

class Userdata(BaseModel):
    full_name: str
    username: str
    age: int


input_data = {"full_name": "Rafay" , "username": "Javaed" , "age": 6}

user = Userdata(**input_data)

print(user)