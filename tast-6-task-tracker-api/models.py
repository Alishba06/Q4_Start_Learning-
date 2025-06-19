from pydantic import BaseModel, EmailStr, constr, validator
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20) # type: ignore
    email: EmailStr

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    due_date: date
    user_id: int

    @validator("due_date")
    def due_date_cannot_be_past(cls, v):
        from datetime import date
        if v < date.today():
            raise ValueError("due_date must be today or in the future")
        return v
