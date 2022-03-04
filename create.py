from application import db                      #this imports the db variable from the application folder - the create file must be saved outwith the application folder

db.drop_all()                                   #you must save and run this file to create your database first, before running the app file.
db.create_all()                                 