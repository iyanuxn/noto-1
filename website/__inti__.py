from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from datetime import datetime
from flask_login import LoginManager
# Creating a database object and setting the name of the database.
db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    """
    It creates a Flask app and sets the secret key to an empty string
    :return: The app object is being returned.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='abcdefghi'
    # Setting the database URI and initializing the database.
    app.config['SQLALCHEMY_DATABASE_URI']=f"sqlite:///{DB_NAME}"
    # Initializing the database.
    
    db.init_app(app)
    
    
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    
    create_database(app)
    
    login_manager= LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
   # Checking if the database exists. If it doesn't, it creates it.
    if not path.exists('.website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')
