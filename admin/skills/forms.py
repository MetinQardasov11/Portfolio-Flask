from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class SkillsForm(FlaskForm):
    skill_name = StringField('skill_name')
    skill_percent = IntegerField('skill_percent')
    submit = SubmitField('submit')