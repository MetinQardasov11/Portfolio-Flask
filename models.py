from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Home(db.Model):
    __tablename__ = 'home'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(200))
    content = db.Column(db.String(200))
    github_link = db.Column(db.String(200))
    linkedin_link = db.Column(db.String(200))
    facebook_link = db.Column(db.String(200))
    email = db.Column(db.String(200))
    
class About(db.Model):
    __tablename__ = 'about'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(200))
    job = db.Column(db.String(200))
    birthday = db.Column(db.String(200))
    website = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    city = db.Column(db.String(200))
    age = db.Column(db.String(200))
    email = db.Column(db.String(200))
    description = db.Column(db.Text)

class Skills(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skill_name = db.Column(db.String(200))
    skill_percent = db.Column(db.Integer)
    
class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    speciality = db.Column(db.String(200))
    start_date = db.Column(db.Integer)
    end_date = db.Column(db.Integer)
    university = db.Column(db.String(200))
    description = db.Column(db.Text)

class Experience(db.Model):
    __tablename__ = 'experience'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_title = db.Column(db.String(200))
    start_date = db.Column(db.String(200))
    end_date = db.Column(db.String(200))
    company_name = db.Column(db.String(200))
    description = db.Column(db.Text)

class ProjectCategory(db.Model):
    __tablename__ = 'project_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    projects = db.relationship('Projects', backref='category', lazy=True)

class Projects(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    category_id = db.Column(db.Integer, db.ForeignKey('project_category.id'), nullable=False)
    image = db.Column(db.String(200))
    link = db.Column(db.String(200))

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    email = db.Column(db.String(200))
    github_link = db.Column(db.String(200))
    linkedin_link = db.Column(db.String(200))

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    is_logged_in = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
