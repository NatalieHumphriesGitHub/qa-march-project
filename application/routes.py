from flask import redirect, url_for, render_template, request                                               
from application import app, db                                                   
from application.models import Room, Plant   
from application.forms import AddPlant, AddRoom                            

#homepage route

@app.route('/')
def home():
    return render_template('index.html')


#add a room type route

@app.route('/add-room', methods = ['GET', 'POST'])
def add_room():
    form = AddRoom()
    if request.method == 'POST':
        room_name = form.room_name.data
        new_room = Room(room_name = room_name)
        db.session.add(new_room)
        db.session.commit()
        return render_template('room-added.html')
    return render_template('add-room.html', form = form)







# #add a plant route
# @app.route('add-plant', methods = 'GET', 'POST')
# def add_plant():
#     rooms = Room.query.all()                                    #this is pulling through all the rooms