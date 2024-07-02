from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class EducationForm(FlaskForm):
    speciality = StringField('speciality')
    start_date = StringField('start_date')
    end_date = StringField('end_date')
    university_address = StringField('university_address')
    description = TextAreaField('description')
    submit = SubmitField('Submit')