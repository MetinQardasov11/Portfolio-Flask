from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ContactForm(FlaskForm):
    address = StringField("address")
    phone = StringField("phone")
    email = StringField("email")
    github_link = StringField("github_link")
    linkedin_link = StringField("linkedin_link")
    submit = SubmitField("Submit")