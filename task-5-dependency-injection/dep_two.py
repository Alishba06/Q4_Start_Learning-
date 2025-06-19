
class Database:

    def connect(slef):
        return "Connect to Database"
    

class Service:

    def __init__(self , db :Database):
        self.db = db

    def get_data(self):
        return self.db.connect()
    
# Usage

db = Database()

service = Service(db)
print(service.get_data())