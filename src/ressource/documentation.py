
from flask_restful import Resource
from flask import render_template 
# 

class Documentation(Resource) : 
    def post(self) : 
        return render_template('index.html')
    def get(self) : 
        return render_template('index.html')

