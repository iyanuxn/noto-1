from flask import Blueprint, jsonify, render_template, request,flash
from flask_login import login_required,current_user
from .models import Note
from website.__inti__ import db
import json
"""
The function home() returns the string "Test" when the user visits the root of the website
    :return: A string
    """

views = Blueprint('views',__name__,template_folder='/website/templates')

@views.route('/Home',methods=['GET'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/Note', methods=['POST','GET'])
@login_required 
def note():
    if request.method == 'POST':
        note =request.form.get('note')
        if len(note)< 1:
            flash('Note is too short!', category='error')
        else:
            new_note= Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note has been saved ', category='success')
    return render_template("Notes.html",user=current_user)


@views.route('/')
def landing():
    return render_template("base.html")

@views.route('/delete-note', methods=['POST'])
def delete_note():	
    note =json.loads(request.data)
    noteId =note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})