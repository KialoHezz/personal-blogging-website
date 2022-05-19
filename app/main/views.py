from flask import render_template,redirect,request,url_for,abort
from flask_login import login_required
from ..models import User

from . import main



@main.route('/')
@login_required
def index():
    
    title = 'Personal Blog Website'

    

    return render_template('index.html', title=title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user=user)