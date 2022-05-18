import re
from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__,template_folder='/website/templates')

@auth.route('/login', methods=['GET','POST'])
def  login():

    return render_template('login.html')

@auth.route('/logout')
def logout():
    return"<p>logout<p>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email')
        firstName= request.form.get('firstName')
        lastName= request.form.get('lastName')
        password1= request.form.get('password1')
        password2= request.form.get('password2')

        if len(email) <4:
            flash('Email should be greater than 4 characters', category='error')
        elif len(firstName)<2:
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
        elif not re.search('[!@#$]',password1):
            flash('password must contain at least 1  special character (!@#$)', category='error')
        else:
            flash('Account has been created', category='success')
        
    return render_template('sign_up.html')