from . import db
# for secure
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
# from datatime import datetime



# callback function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(200))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(300))
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User {self.username} {self.email} {self.password_secure}'

    @property
    def password(self):
        raise AttributeError('Unable to read the password')

    @password.setter
    def password(self,password):
        self.password_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.password_secure,password)


class Role(db.Model, UserMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'


class Qoutes:
    '''
    Qoutes class to define Quotes object

    '''
    def __init__(self,id,author,quote,permalink):
        self.id = id
        self.author = author
        self.quote = quote
        self.permalink = permalink

class Post(db.Model, UserMixin):
      __tablename__ = 'posts'
      id = db.Column(db.Integer, primary_key=True)
      title = db.Column(db.String(100), nullable=False)
      content = db.Column(db.Text, nullable=False)
      category = db.Column(db.Text, nullable=False)
    #   date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    #   comments = db.relationship('Comment', backref='post', lazy=True)

      def __repr__(self):
            return f"Post('{self.title}', '{self.content}', '{self.category}', '{self.date_posted}')"