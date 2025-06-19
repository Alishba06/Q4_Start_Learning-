
from fastapi import FastAPI , Depends

app = FastAPI()

class Database:

    def connect(self):
        return "Connect to DataBase"

    def disconnect(self):
        return "Disconnect to DataBase"

def get_database():
    db = Database()
    
    try:
        yield db
    finally:
        db.disconnect

@app.get("/car")

def reag_car(db=Depends(get_database)):
    return {"message" : "Hello Doller"}