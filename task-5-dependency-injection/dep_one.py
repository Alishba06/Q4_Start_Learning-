
class DataBase:
    def connect(self):
        return "Connect to DataBase"
    

class Service:

    def __init__(self):
        self.db = DataBase()  # tight coupling

    def get_data(self):
        return self.db.connect()
    

# Usage

service = Service

print(service.get_data())
    


