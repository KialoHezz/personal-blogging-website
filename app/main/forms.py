from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,BooleanField,PasswordField
import email
from wtforms.validators import DataRequired,EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Enter your username',validators=[DataRequired()])
    email = StringField('Enter your email address', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators=[DataRequired()])
    submit = SubmitField('Register')
    

class LoginForm(FlaskForm):
    email = StringField('Enter your email address',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(), EqualTo('password')])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')