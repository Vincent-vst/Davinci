
from flask_restful import Resource

"""
This is the ressource file. 
It represent what we SEND to the client. 
"""

class Transcript(Resource) : 
    def get(self) : 
        return {"transcript" : "hello", "quality" : "mp3", "kHz" : 48000}