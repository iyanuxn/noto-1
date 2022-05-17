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