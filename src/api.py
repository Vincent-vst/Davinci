from flask import Flask 
from flask_restful import Api

# TODO : change the import method 
import ressource.transcript as transcript
import ressource.documentation as documentation
import ressource.database as database 

from ressource.transcript import Transcript
from ressource.documentation import Documentation
from ressource.database import Database

app = Flask(__name__)
api = Api(app)
api.add_resource(Transcript, "/transcript/<string:audio>")
api.add_resource(Documentation, "/documentation")
api.add_resource(Database, "/database")

if __name__ == "__main__" :  
    app.run(debug=True, host='0.0.0.0')  
