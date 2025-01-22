from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initializing the database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # Create and configure the Flask application so that it can be run
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'IWHSEJFIGVKJMedhfdi esdfhmjiswejdnhf wsedf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)



    # Importing the views and auth files and registering the blueprints so that the routes can be accessed by the app/navbar
    from .veiws import veiws
    from .auth import auth

    app.register_blueprint(veiws, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .model import User, Note
    
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app) # Initialize the database with the app so that the user and relavant data can be loaded 

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')