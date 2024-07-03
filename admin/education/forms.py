from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField

class EducationForm(FlaskForm):
    speciality = StringField('speciality')
    start_date = IntegerField('start_date')
    end_date = IntegerField('end_date')
    university = StringField('university')
    description = TextAreaField('description')
    submit = SubmitField('Submit')