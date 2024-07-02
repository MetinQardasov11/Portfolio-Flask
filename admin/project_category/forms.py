from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ProjectCategoryForm(FlaskForm):
    name = StringField('name')
    submit = SubmitField('submit')