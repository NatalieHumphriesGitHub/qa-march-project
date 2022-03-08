from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError


#form to add plants to the database

class AddPlant(FlaskForm):
    plant_name = StringField("Plant Name", validators=[DataRequired()])
    plant_desc = StringField("Plant Description")
    flowers = SelectField("Does it flower?", choices = [('does', 'Yes'), ('does not', 'No')])
    watering_req = SelectField("How much watering is required", choices = [('low', 'A little'), ('medium', 'Some'), ('high', 'A lot')])
    room_id = SelectField("Which room is it in?", choices = [])
    submit = SubmitField("Submit")


#form to add rooms to the database

class AddRoom(FlaskForm):
    room_name = StringField("Room Name")
    submit = SubmitField("Add Room")



