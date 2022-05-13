from flask import Flask

def create_app():
    # init the application
    app = Flask(__name__)


    # register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)




    return app