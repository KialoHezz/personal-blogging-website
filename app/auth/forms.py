from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,validators
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
import email_validator




class RegisterForm(FlaskForm):
    username = StringField('Enter your username',validators = [DataRequired()])
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Enter your email address',validators=[DataRequired()])
    password_secure = PasswordField('Password',validators=[DataRequired(),EqualTo('password')])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

    