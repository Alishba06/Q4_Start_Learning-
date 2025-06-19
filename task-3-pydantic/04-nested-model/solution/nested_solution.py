
from pydantic import BaseModel

class Lesson(BaseModel):
    title:str
    lesson_id:int


class Course(BaseModel):
    course_id:int
    name:str
    lessons: list[Lesson]