from flask import Flask 
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from ressource.transcript import Transcript
from ressource.documentation import Documentation
from ressource.database import Database
# from ressource.video import Video

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///davinci.db'
db = SQLAlchemy(app)
api.add_resource(Transcript, "/transcript/<string:audio>")
api.add_resource(Documentation, "/documentation", methods=['GET', 'POST'])
api.add_resource(Database, "/database")
# api.add_resource(Video, "/video")


if __name__ == "__main__" :  
    app.run(debug=True, host='0.0.0.0')  
