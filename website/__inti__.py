from flask import Flask

def create_app():
    """
    It creates a Flask app and sets the secret key to an empty string
    :return: The app object is being returned.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='abcdefghi'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
