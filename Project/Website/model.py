from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Note model to store note data with id as foriegn key so that no other note in the database is changed when one is touched, along with date created with a foreign key to the User model to link the notes to the user
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# User model to store user data with id as the primary key, email as a unique string, password as a string, first name as a string, and notes as a child column to the Note model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')