from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

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

    # this until "return app" is for not seeing certain things until we login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # where should the user go if we are NOT logged in (remember its name of file name of function)
    login_manager.init_app(app)

    @login_manager.user_loader # this is telling flask how we load a user
    def load_user(id):
        return User.query.get(int(id)) # .get = look for primary key and check if its equal to what we passed

    return app

def create_database(app):
    if not path.exists('website/' + db_name):
        with app.app_context(): # makes the application context -> flask doesnt doesn't automatically know which application is "active" unless you explicitly push the application context 
            db.create_all() 
        print('Created databse')