from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST']) #methods is for the different https methods like get post, delete, go to url -> get method, hit submit button ->post method
def login():
    # return render_template("login.html")
    # data = request.form # request inside root = info about the request that was sent to access the root
    # print(data)
    return render_template("login.html", text = "testing", user="Arnav", boolean = True) #inside login.html we can access the variable text


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error') # cateogry = name whatever u want -> just a var now
        elif len(firstName) < 1:
            flash('First name must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('Passowrds don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # add user to database
            flash('Account created!', category='success')

    return render_template("sign_up.html")
