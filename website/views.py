# where the users can go to that isnt related to authentication

from flask import Blueprint, render_template 
# render template to render a html template

# blueprints allow roots and allow views to be split up into many files

views = Blueprint('views', __name__) # name it to the same thing as the file.. u dont need to but

@views.route('/')
def home(): # when we go to our url and just type '/' it will go to home function
    return render_template("home.html")