this website templae is for a note website with login details
accounts can be created with diffrent dbs
this is built with flask


try using typing DNA for  biometrics authenthicator


main.py is the  code to run when you want to run the website
__init__ is what will make the website folder as a python package

from main.py
line 5 only if we run main.py is the line going to be executed so that if we import another main.py file the  web server will not run 
line 6 is used to rerun the webserver
that line should be off during production
and on during development so as to show changes to the sever

the py files auth is for login and security authenthications 
the py file  views is mainly for none credential pages


in template 
the base.html is the theme of the website  after which it wil be overwritten/overlap over the base.html file
the {%%}allows python codes to be run in the html code 
this code was written at the advent of pyscript 
the {% block title %} defines the block in the base template and will make it interchangeable

FOR THE FRONT END DEVELOPER 
put all static files (e.g javascript, css, images, files that dont change ) into the static folder
 
 example to load the files into the the html file are in the html file


'static' - the foldername
 the "{{}}" is used to add python codes into the website

 {% extends "base.html"%} this means that the predestined template is going to be the same as base.html and any blocks defined in base html can be over written

if you want to pass a variable from the back end to the front end(mini reminder)

def home():
    return render_template("home.html" text="text you want to pass to the front end")

    and at the front end you will use a python method codde
    like {{ text }} and your variable should be able to be called from the back-end to the front

to write an if statement in the html section
{% if  boolean == True %}
what you want to make happen if its true 
{% endif % }




the names in the front end should be properly defined if they are data types that are going to be taken into the backend



HTTP requests(method not allowed)
these are various call back methods
-get- is to load or retrive information
-post- database or state change
-put
-delete
-update
 the point of these request is to know what type of request are being sent to your website

by default after inputing methods into the python request but you can other requests 
the request variables holds access to the request sent by the form


a MultiDict is a sub-class of Dictionary that can contain multiple values for the same key, unlike normal Dictionaries.  It is used because some form elements have multiple values for the same key and it saves the multiple values of a key in form of a list.

    "data = request.form
    print(data) "put this into th request route line to see if the request is entering 

message flashing 
when using category , you can name the error or success messages how ever you like


on model.py 
to create a class for data to be stored 
class ..class name(db.model) It will inherit it from db.model
then add the foreign keys(note this is for 1 to many)

app.config['SQLALCHEMY_DATABASE_URI']=f"sqlite:///{DB_NAME}" this imports the sql databse and gives it a name
   # Checking if the database exists. If it doesn't, it creates it.
    if not path.exists('.website/' + DB_NAME):
        db.create_all(app=app)

from werkzeug.security import generate_password_hash,check_password_hash 
this is because we cannot save a password as plain text


a hashing fuction is a one way fuction that does not have an inverse
eg
x -> y
f(x) = x+1
this function has an inverse
this means that if you were given the out put then you can get the input 
to understand more , read on hashing functions

method='sha256 this is just a type of hashing function '
read more on it

