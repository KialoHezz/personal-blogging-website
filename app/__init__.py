from flask import Flask
import os
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager,login_manager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    # init the application
    app = Flask(__name__)

    
    app.config.from_object(config_options[config_name])

    # register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # register auth blueprint
    #  pass in a url_prefix argument that will add a prefix to all the routes registered with that blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # init the extension blueprint
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)


    return app