from flask import render_template,redirect,url_for,flash,request

from .. import db
from ..models import User
from . import auth
from .forms import RegisterForm,LoginForm
from flask_login import login_user,logout_user,login_required



@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, password_secure = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
       
    return render_template('auth/register.html',form = form)




@auth.route('/login',methods=['GET','POST'])
def login():
    logform = LoginForm()
    if logform.validate_on_submit():
        user = User.query.filter_by(email = logform.email.data).first()
        if user is not None and user.verify_password(logform.password_secure.data):
            login_user(user,logform.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Personal blog login"
    return render_template('auth/login.html',logform = logform,title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))