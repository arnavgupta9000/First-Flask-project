from . import db # import from current package (website folder) import the db object
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id will autoincrement
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default=func.now()) # timezone = True -> store timezone info as well, func ->gets current date and time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # match db.Integer with user_id type # note that user is lowercase

class User(db.Model, UserMixin): # name of object then inherit from db.Model and only for user we need UserMixin 
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True) # String(150) = max length, no 2 users can have the same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # everytime we create a note -> add into Note the new id # note that its capital
