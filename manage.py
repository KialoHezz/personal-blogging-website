from app import create_app,db
from app.models import User,Role
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand

# create instance
# app = create_app('production')
app = create_app('development')

# create flask-script shell
manager = Manager(app)
manager.add_command('db',Manager)

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand) 

@manager.shell
def make_shell():
    return dict(app=app, db=db, User=User)




if __name__ == '__main__':
    manager.run()