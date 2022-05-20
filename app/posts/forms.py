from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,BooleanField,SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
      title = StringField('Title', validators=[DataRequired()])
      content = TextAreaField('Content', validators=[DataRequired()])
      category = SelectField('Categories', choices=[('Music'), ('Quotes'), ('Dances'), ('Experience')], validators=[DataRequired()])
      submit = SubmitField('Add Post')