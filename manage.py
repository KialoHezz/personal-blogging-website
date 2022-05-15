from app import create_app,db
from app.models import User
from flask_script import Manager

# create instance
app = create_app()

# create flask-script shell
manager = Manager(app)
manager.add_command('db')


@manager.shell
def make_shell():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    app.run()