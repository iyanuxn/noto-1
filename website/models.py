# Importing the db and UserMixin from the current directory.
from website.__inti__ import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
# It creates a table called Note in the database.
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000000000))
    date =db.Column(db.DateTime(timezone=True), default=func.now())
   # Creating a column called user_id in the Note table. It is also creating a relationship between
   # the Note table and the User table.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# It creates a class called User that inherits from db.Model and UserMixin. It also creates a table
# called users with the following columns: id, email, password, first_name, and notes.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email =db.Column(db.String(200), unique=True)
    password = db.Column(db.String(150))
    first_Name = db.Column(db.String(150))
   # Creating a relationship between the User table and the Note table.
    notes=db.relationship('Note')

