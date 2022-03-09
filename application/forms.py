from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from application.models import Room, Plant



#form for a keyword search

class SearchKeyWord(FlaskForm):
    keyword = StringField("Enter your keyword", validators =[DataRequired()])
    submit = SubmitField("Search")

#form to add plants to the database

class AddPlant(FlaskForm):
    plant_name = StringField("Plant Name", validators=[DataRequired()])
    plant_desc = StringField("Plant Description")
    flowers = SelectField("Does it flower?", choices = [('does', 'Yes'), ('does not', 'No')])
    watering_req = SelectField("How much watering is required", choices = [('low', 'A little'), ('medium', 'Some'), ('high', 'A lot')])
    room_id = SelectField("Which room is it in?", choices = [])
    submit = SubmitField("Submit")


#form to validate checking whether the room already exists - need to import the Room model because using validators to check it
#this needs to above the class you're checking

class RoomCheck():
    def __init__(self, message = "Room already exists"):
        self.message = message

    def __call__(self, form, field):
        if field.data in [room.room_name for room in Room.query.all()]:
            raise(ValidationError(self.message))


#form to add rooms to the database

class AddRoom(FlaskForm):
    room_name = StringField("Room Name", validators = [RoomCheck()])
    submit = SubmitField("Add Room")





