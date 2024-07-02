from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ExperienceForm(FlaskForm):
    job_title = StringField('job_title')
    start_date = StringField('start_date')
    end_date = StringField('end_date')
    company_name = StringField('company_name')
    make_done = StringField('make_done')
    submit = SubmitField('Submit')