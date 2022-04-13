from flask_restful import Resource 
import sqlite3  
from database_controller import *

class Database(Resource): 
    def get(self) : 
        return "hello"


print_db()
