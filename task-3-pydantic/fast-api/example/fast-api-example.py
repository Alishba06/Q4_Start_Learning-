
from fastapi import FastAPI , Depends
from pydantic import BaseModel , EmailStr

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    app_name: str = "Fast API"
    admin_email: EmailStr = "admin@example.com"

def get_app_name():
    return ShowUser

@app.post('/signup')
def signup(user: User):
    return {"message": f"User {user.name} created successfully"}


@app.get('/userr')
def get_show_user(user: ShowUser = Depends(get_app_name)):
    return user
