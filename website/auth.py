import re

from flask import Blueprint, redirect,render_template,request,flash,redirect,url_for

from website.__inti__ import db
from .models import User
# A function that is used to generate a password hash.
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint('auth',__name__,template_folder='/website/templates')

@auth.route('/login', methods=['GET','POST'])
def  login():
    if request.method == 'POST':
        email =request.form.get('email')
        password =request.form.get('password')
        
        user= User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in successfully!', category='success')
                
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
            
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return"<p>logout<p>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email')
        first_Name= request.form.get('firstName')
        last_Name= request.form.get('lastName')
        password1= request.form.get('password1')
        password2= request.form.get('password2')

        user= User.query.filter_by(email=email).first()
        if user:
            flash('Account with that email already exists.', category='error')
        elif len(email) <4:
            flash('Email should be greater than 4 characters', category='error')
        elif len(first_Name)<2:
            flash('Name is too short',category='error')
        elif password1 != password2:
            flash("passwords do not match",category='error')
        elif len(password1)<7:
            flash('password is too short')
        elif not re.search('[a-z]', password1):
            flash('password must contain at least 1 alphabets', category='error')
        elif not re.search('[0-9]', password1 ):
            flash('password must contain at least 1 number', category='error')
        elif not re.search('[A-Z]',password1):
            flash('password must contain at least 1 capital letter', category='error')
        elif not re.search('[!@#$_-]',password1):
            flash('password must contain at least 1  special character (!@#$)', category='error')
        else:
            new_user =User(email=email, first_Name=first_Name, last_Name=last_Name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account has been created', category='success')
            return redirect(url_for('views.landing'))
        
    return render_template('sign_up.html')