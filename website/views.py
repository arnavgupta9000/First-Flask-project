# where the users can go to that isnt related to authentication

from flask import Blueprint, render_template, request, flash, jsonify

from flask_login import login_required, current_user # for user interactions ; why we needed usermixing in models file -> for current_user;

from .models import Note
from . import db

import json

# render template to render a html template

# blueprints allow roots and allow views to be split up into many files

views = Blueprint('views', __name__) # name it to the same thing as the file.. u dont need to but

@views.route('/', methods=['GET', 'POST'])
@login_required # cant get to home page unless u log in
def home(): # when we go to our url and just type '/' it will go to home function
    if request.method == 'POST':
        note=request.form.get('note')

        if len(note) < 1:
            flash('Note is to short', category = 'error')
        else:
            new_note = Note(data=note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added", category = 'success')

    return render_template("home.html", user=current_user) # in our template reference this current_user and check if its authenticated 

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) # string what we sent from js -> turn to dict -> then access noteId
    noteId = note['noteId']
    note = Note.query.get(noteId) # look for note with that id

    if note:
        if note.user_id == current_user.id: # if the user owns this note
            db.session.delete(note) # how u delete stuff from databse, query it then delete it
            db.session.commit()
    return jsonify({}) # turn into json object that we can return... (must return something ig)