from flask import redirect, url_for, render_template, request                                               
from application import app, db                                                   
from application.models import Room, Plant   
#from application.forms import AddToDo, CreateProject                                 

#homepage route

@app.route('/')
def home():
    return render_template('index.html')