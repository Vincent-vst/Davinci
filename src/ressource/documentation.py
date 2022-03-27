
from flask_restful import Resource

class Documentation(Resource) : 
    def get(self) : 
        return "API Documentation : In order to use this API, do ... " 
