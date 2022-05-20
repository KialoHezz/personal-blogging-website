from flask import render_template,redirect,url_for,flash,request,Blueprint

from .. import db
from app.models import User,Post
from . import auth
from app.posts.forms import PostForm
from flask_login import login_user,logout_user,login_required,current_user
from flask import session



posts = Blueprint('posts', __name__)


@posts.route('/add-post', methods=['GET', 'POST'])
# @login_required
def addPost():
      form = PostForm()
      if form.validate_on_submit():
            post = Post(title=form.title.data, content=form.content.data, author=current_user, category=form.category.data)
            db.session.add(post)
            db.session.commit()
            flash('Your Post has been added', 'success')
            return redirect(url_for('main.index'))
      return render_template('posts/new-post.html', title='Add Post', form=form, legend='New Post')

