from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class HomeForm(FlaskForm):
    full_name = StringField('full_name')
    content = StringField('content')
    github_link = StringField('github_link')
    linkedin_link = StringField('linkedin_link')
    facebook_link = StringField('facebook_link')
    email = StringField('email')
    submit = SubmitField('submit')