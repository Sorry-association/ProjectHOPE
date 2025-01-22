from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
import json

from Website.model import Note, db

# Create a Blueprint for the views routes using the imported Flask Blueprint class
veiws = Blueprint('veiws', __name__)

#Route for the home page, we made it so it requires login to access the page
@veiws.route('/')
@login_required
def home():
    # Render the home page template and pass the current user to the template
    return render_template("home.html", user=current_user)


# Route for the notebook page, supports GET and POST methods, requires login
@veiws.route('/notebook', methods=['GET', 'POST'])
@login_required
def notebook():
    if request.method == 'POST': 
        note = request.form.get('note') 

        # Validate the note length and add the note to the database if it is valid 
        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
        # Render the notebook page template and pass the current user to the template so that it loads the saved notes of the user.
    return render_template("notebook.html", user=current_user)

@veiws.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return redirect(url_for('notebook'))

    return jsonify({})