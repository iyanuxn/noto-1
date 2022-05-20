from flask import Blueprint, render_template
from flask_login import login_required,current_user
"""
The function home() returns the string "Test" when the user visits the root of the website
    :return: A string
    """

views = Blueprint('views',__name__,template_folder='/website/templates')

@views.route('/Home')
@login_required
def home():
    return render_template("home.html", user=current_user)
@views.route('/main') 
def main():
    return render_template("Notes.html")
@views.route('/')
def landing():
    return render_template("base.html")