from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Plant, Room


class TestBase(TestCase):                       
    def create_app(self):                       
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',   
            SECRET_KEY = "test secret key",
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )

        return app

    def setUp(self): # Run before each test - this is creating a new database with the below information
        db.create_all()
        sample_room = Room(room_name = "Test Room")                     #create a sample room
        sample_plant = Plant(plant_name = "Test Plant", plant_desc = "A sample plant for testing", flowers = "does", watering_req = "low", room_id = 1) 
        sample_plant2 = Plant(plant_name = "Test Plant2", plant_desc = "Another sample plant for testing", flowers = "does not", watering_req = "low", room_id = 1)         
        
        db.session.add(sample_room)   
        db.session.add(sample_plant)  
        db.session.add(sample_plant2)
        db.session.commit()           

    def tearDown(self):                
        db.session.remove()             
        db.drop_all()                   

#testing that the homepage asks "What would you like to do today?" and has all the links required

class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'What would you like to do today?', response.data)

    def test_home_update(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Update or delete a plant', response.data)

    def test_home_add(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Add a new plant', response.data)

    def test_home_addroom(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Add a new room', response.data)

    def test_home_viewall(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'View your plants', response.data)    

#testing for adding a new room

class TestAddRoom(TestBase):
    def test_addroom_get(self):
        response = self.client.get(url_for('add_room'))
        self.assert200(response)
        self.assertIn(b'Room Name', response.data)
    
    def test_addroom_post(self):
        response = self.client.post(
            url_for('add_room'),                        #always want a url to check
            data = dict(room_name = "New Room"))        #always want to add the data to check that the post is happening
        self.assert200(response)                        #always be 200
        self.assertIn(b'Room added successfully!', response.data) #check success message is correct
        self.assertNotEqual(Room.query.filter_by(room_name = "New Room").first(),None) #checking the db for the new info this is checking that when you filter the rooms for the new plant, it is not equal to none)

# #testing for adding a new plant

class TestAddPlant(TestBase):
    def test_addplant_get(self):
        response = self.client.get(url_for('add_plant'))
        self.assert200(response)
        self.assertIn(b'Plant Name', response.data)
    
    def test_addplant_post(self):
        response = self.client.post(
        url_for('add_plant'),
        data = dict(plant_name = "New Plant", plant_desc = "A new plant for testing", flowers = "does", watering_req = "low", room_id = 1 ))
        self.assert200(response)
        self.assertIn(b'Plant has been added successfully!', response.data)
        self.assertNotEqual(Plant.query.filter_by(plant_name="New Plant").first(), None)

#testing for view all plants

class TestViewAllPlants(TestBase):
    def test_viewall_get(self):
        response = self.client.get(url_for('view_all'))
        self.assert200(response)
        self.assertIn(b'Test Plant', response.data)

#testing for view all rooms

class TestViewAllRooms(TestBase):
    def test_viewallrooms_get(self):
        response = self.client.get(url_for('view_rooms'))
        self.assert200(response)
        self.assertIn(b'Test Room', response.data)

#testing for updating plants information

class TestUpdatePlant(TestBase):
    def test_updateplant_get(self):
        response = self.client.get(url_for('update_plant', pk = 1))
        self.assert200(response)
        self.assertIn(b'Plant Name', response.data)

    def test_updateplant_post(self):
        response = self.client.post(
        url_for('update_plant', pk = 1),
        data = dict(plant_name = "Updated Plant", plant_desc = "An updated plant for testing", flowers = "does", watering_req = "low", room_id = 1 ))
        self.assert200(response)
        self.assertIn(b'Plant has been updated successfully!', response.data)
        self.assertNotEqual(Plant.query.filter_by(plant_name = "Updated Plant").first(), None)

#testing for find a plant to update

class TestChoosePlant(TestBase):
    def test_chooseplant_get(self):
        response = self.client.get(url_for('choose_plant_update'))
        self.assert200(response)
        self.assertIn(b'Which plant would you like to update?', response.data)

#testing for deleting plant

class TestDeletePlant(TestBase):
    def test_deleteplant_get(self):
        response = self.client.get(url_for('delete_plant', pk = 2))
        self.assert200(response)
        self.assertIn(b'Plant has been deleted successfully!', response.data)
        self.assertEqual(Plant.query.filter_by(plant_name = 'Test Plant2').first(),None)

