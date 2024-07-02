from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField

class ProjectForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    image = FileField('image')
    link = StringField('link')
    submit = SubmitField('submit')
