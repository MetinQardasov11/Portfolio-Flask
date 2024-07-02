from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField

class AboutForm(FlaskForm):
    image = FileField("image")
    job = StringField("job")
    birthday = StringField("birthday")
    website = StringField("website")
    phone = StringField("phone")
    city = StringField("city")
    age = StringField("age")
    email = StringField("email")
    description = TextAreaField("description")
    submit = SubmitField("Submit")