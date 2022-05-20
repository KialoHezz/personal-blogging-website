from flask import render_template,redirect,request,url_for,abort,Blueprint
from flask_login import login_required
from ..models import User
from flask import Flask, session

from . import main


main = Blueprint('main', __name__)

@main.route('/')
def index():
    
    title = 'Personal Blog Website'

    

    return render_template('index.html', title=title)
    

@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/profile/<uname>')
def profile(uname):
    if 'email' not in session:
        return redirect(url_for('main.home'))

    user = User.query.filter_by(email = session['email'],username = uname).first()

    if user is None:
        return redirect(url_for('signin'))
    else:
        return render_template('profile.html')

    return render_template('profile/profile.html', user=user)



@main.route('/home')
def home():
    
    


    return render_template('index.html')