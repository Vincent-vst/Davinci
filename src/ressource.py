
from flask_restful import Resource

"""
This is the ressource file. 
It's here where we'll figure out what we SEND and RECEIVE from the client.

"""

class Transcript(Resource) : 
    def get(self) : 
        # what we send to the client 
        return {"transcript" : "hello", "quality" : "mp3", "kHz" : 48000}

    def post(self) : 
        # what we receive from the client
        return {"data" : "no post method yet"}