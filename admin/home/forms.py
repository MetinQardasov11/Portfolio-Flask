from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class HomeForm(FlaskForm):
    full_name = StringField('full_name')
    description = StringField('description')
    github_link = StringField('github')
    linkedin_link = StringField('linkedin')
    facebook_link = StringField('facebook')
    email_link = StringField('email')
    submit = SubmitField('submit')