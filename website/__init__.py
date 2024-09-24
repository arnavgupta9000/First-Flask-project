from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy() # init the database
db_name = "database.db"

# __init__py -> whenever you put that into a package it becomes a python package

def create_app():
    app = Flask(__name__) # __name__ = represents name of file that was run
    app.config['SECRET_KEY'] = 'hello there' # encrypts the data with whatever string u want
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}' # sql database is located at sqlite:///{db_name}
    db.init_app(app) # make the database

    from .views import views # importing the variable
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # just the prefix http://127.0.0.1:5000/ like u see that '/' at the end.. its just to omit that

    from .models import User, Note

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + db_name):
        with app.app_context(): # makes the application context -> flask doesnt doesn't automatically know which application is "active" unless you explicitly push the application context 
            db.create_all() 
        print('Created databse')