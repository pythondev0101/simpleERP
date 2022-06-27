from flask import Flask
from flask_login import LoginManager
from flask_pymongo import PyMongo
from config import APP_CONFIG


MONGO = PyMongo()
LOGIN_MANAGER = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(APP_CONFIG[config_name])

    MONGO.init_app(app)
    LOGIN_MANAGER.init_app(app)
    
    LOGIN_MANAGER.login_view = 'bp_auth.login'
    LOGIN_MANAGER.login_message = "You must be logged in to access this page."

    with app.app_context():
        from app.main import bp_main
        from app.auth import bp_auth
        from app.core import cli
        
        app.register_blueprint(bp_main, url_prefix='/')
        app.register_blueprint(bp_auth, url_prefix='/auth')
    return app
