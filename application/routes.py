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

#add a plant route

@app.route('/add-plant', methods = ['GET', 'POST'])
def add_plant():
    rooms = Room.query.all()
    form = AddPlant()
    form.room_id.choices.extend([(room.pk, str(room)) for room in rooms])
    if request.method == 'POST':
        plant_name = form.plant_name.data
        plant_desc = form.plant_desc.data
        flowers = form.flowers.data
        watering_req = form.watering_req.data
        room_id = int(form.room_id.data)
        new_plant = Plant(plant_name = plant_name, plant_desc = plant_desc, flowers = flowers, watering_req = watering_req, room_id = room_id)
        db.session.add(new_plant)
        db.session.commit()
        return render_template ('plant-added.html')
    return render_template('add-plant.html', form = form)


#view all plants

@app.route('/view-all')
def view_all():
    plants = [str(plant) + ": Located in the " + str(plant.room).lower() for plant in Plant.query.order_by(Plant.pk).all()]
    return render_template ('view-all.html', plants = plants)
