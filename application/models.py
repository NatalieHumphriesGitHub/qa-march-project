from application import db

class Room(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    room_name = db.Column(db.String(30))
    plants_room = db.relationship('Plant', backref='room')
def __str__(self):
    return f"{Self.room_name}"


class Plant(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    plant_name = db.Column(db.String(50))
    plant_desc = db.Column(db.String(500))
    flowers = db.Column(db.String(10))
    watering_req = db.Column(db.String(20))
    room_id = db.Column(db.Integer, db.ForeignKey('room.pk'))
def __str__(self):
    return f"{plant_name}: {plant_desc}: {flowers} flowers: {watering_req} watering required."