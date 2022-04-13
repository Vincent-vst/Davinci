from flask_restful import Resource 

class Database(Resource): 
    def get(self) : 
        return "hello" 


