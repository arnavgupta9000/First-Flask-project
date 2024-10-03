from flask import Blueprint, render_template, request, flash, redirect, url_for # redirect and url_for -> take the user to somewhere else
from .models import User # remeber the "." means same directory
from werkzeug.security import generate_password_hash, check_password_hash
from . import db # from the __init__.py file
from flask_login import login_user, login_required, logout_user, current_user # for user interactions ; why we needed usermixing in models file -> for current_user;


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST']) #methods is for the different https methods like get post, delete, go to url -> get method, hit submit button ->post method
def login():
    # return render_template("login.html")
    # data = request.form # request inside root = info about the request that was sent to access the root
    # print(data)

    if request.method == 'POST': # signing in
        email = request.form.get('email')
        password = request.form.get('password')

        # check if the email exists in the databse
        user = User.query.filter_by(email=email).first() # user = object so if theres a match we can see any of there attributes
        # the first argument is the tablebase arg
        if user: # found a user
            if check_password_hash(user.password, password): # the . is just accesing there password, .email = email
                flash('Logged in successfully!', category= 'success')
                login_user(user, remember= True) # remember -> remembers there logged in (until u restart flask server, or user clears web history)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect pasword, try again', category = 'error')
            
        else:
            flash('Email does not exist.', category= 'error')
    return render_template("login.html", user=current_user, text = "testing", user1="Arnav", boolean = True) #inside login.html we can access the variable text


@auth.route('/logout')
@login_required # just makes it so we cant access this page unless the user is logged in 
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user: 
            flash('Email already exixtsl', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error') # cateogry = name whatever u want -> just a var now
        elif len(first_name) < 1:
            flash('First name must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('Passowrds don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256', salt_length = 8)) # User is the sql table

            db.session.add(new_user) # add the new user to the database
            db.session.commit() # commit the changes
            login_user(new_user, remember= True)
            flash('Account created!', category='success')

            # redirect to home page
            return redirect(url_for('views.home'))  # note that return redirect(url_for('/')) would also work -> but not dynamic so dont use it basically
            # redirect() -> redirect us to another page
            # the url_for('views.home) means go the views file and find the home function and go to that route ie blueprint name, function name


    return render_template("sign_up.html", user=current_user)
