from flask import Blueprint, render_template
"""
The function home() returns the string "Test" when the user visits the root of the website
    :return: A string
    """

views = Blueprint('views',__name__,template_folder='/website/templates')

@views.route('/Home')
def home():
    return render_template("home.html")
@views.route('/')
def landing():
    return render_template("base.html")