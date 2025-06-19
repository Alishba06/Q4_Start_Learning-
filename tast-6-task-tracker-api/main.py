from fastapi import FastAPI, HTTPException
from models import UserCreate, UserRead, Task
from database import users_db, tasks_db
from utils import validate_status

app = FastAPI()

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    new_user = UserRead(id=user_id, **user.dict())
    users_db.append(new_user)
    return new_user

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = len(tasks_db) + 1
    tasks_db.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status: str):
    validate_status(status)
    for task in tasks_db:
        if task.id == task_id:
            task.status = status
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/users/{user_id}/tasks")
def get_user_tasks(user_id: int):
    user_tasks = [task for task in tasks_db if task.user_id == user_id]
    return user_tasks
