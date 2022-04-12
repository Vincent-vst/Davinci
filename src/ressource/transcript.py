
from flask_restful import Resource

"""
This is the ressource file. 
It's here where we'll figure out what we SEND and RECEIVE from the client.
"""

example_data = {"id" : 1, "audio" : [] , "transcript" : [], "quality" : "mp3", "kHz" : 48000, "depth" : 24}

class Transcript(Resource) : 
    def get(self) : 
        # what we send to the client 
        # Here, we've overwrite the get method because, we don't want to send anything if we haven't received anything
        example_data["transcript"] = "Hello world !"
        return  example_data

    def post(self, audio) : 
        # what we receive from the client
        example_data["audio"] = audio
        return  example_data 