from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating a database object and setting the name of the database.
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    """
    It creates a Flask app and sets the secret key to an empty string
    :return: The app object is being returned.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='abcdefghi'
    # Setting the database URI and initializing the database.
    app.config['SQLACHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Initializing the database.
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
