from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField

class ExperienceForm(FlaskForm):
    job_title = StringField('job_title')
    start_date = IntegerField('start_date')
    end_date = IntegerField('end_date')
    company_name = StringField('company_name')
    description = TextAreaField('description')
    submit = SubmitField('Submit')