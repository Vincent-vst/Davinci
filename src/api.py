from flask import Flask 
from flask_restful import Api
import resource

from ressource import Transcript

app = Flask(__name__)
api = Api(app)
api.add_resource(Transcript, "/transcript")

if __name__ == "__main__" :  
    app.run(debug=True) # don't add debug in a Production environment. 
