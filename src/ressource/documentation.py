
from flask_restful import Resource
from flask import render_template 

class Documentation(Resource) : 
    def get(self) : 
        return render_template('index.html')
