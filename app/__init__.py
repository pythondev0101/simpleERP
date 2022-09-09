from flask import Flask
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_qrcode import QRcode
from flask_wtf.csrf import CSRFProtect
from config import APP_CONFIG

CSRF = CSRFProtect()
MONGO = PyMongo()
LOGIN_MANAGER = LoginManager()
QR_CODE = QRcode()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(APP_CONFIG[config_name])

    CSRF.init_app(app)
    MONGO.init_app(app)
    LOGIN_MANAGER.init_app(app)
    QR_CODE.init_app(app)
    
    LOGIN_MANAGER.login_view = 'auth.login'
    LOGIN_MANAGER.login_message = "You must be logged in to access this page."

    with app.app_context():
        from app.main import bp_main
        from app.auth import bp_auth
        from app.core import cli
        from app.api import bp_api
        from app.datatables import bp_datatables
        
        app.register_blueprint(bp_main, url_prefix='/')
        app.register_blueprint(bp_auth, url_prefix='/auth')
        app.register_blueprint(bp_api, url_prefix='/api')
        app.register_blueprint(bp_datatables, url_prefix='/datatables')
    return app
