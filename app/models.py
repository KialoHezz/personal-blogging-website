from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(200))
    password_secure = db.Column(db.String(300))

    def __repr__(self):
        return f'User {self.username}'