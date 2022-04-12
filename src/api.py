from flask import Flask 
from flask_restful import Api
import ressource.transcript as transcript
import ressource.documentation as documentation

from ressource.transcript import Transcript
from ressource.documentation import Documentation

app = Flask(__name__)
api = Api(app)
api.add_resource(Transcript, "/transcript/<string:audio>")
api.add_resource(Documentation, "/documentation")

if __name__ == "__main__" :  
    app.run(debug=True, host='0.0.0.0') # don't add debug in a Production environment. 
