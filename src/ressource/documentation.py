
from flask_restful import Resource

class Documentation(Resource) : 
    def get(self) : 
        return "<h3>API Documentation</h3>" +  "<a href='https://github.com/Vincent-vst/Davinci/tree/venv'>Read the doc</a> " 
