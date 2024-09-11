from . import app_bp
from flask import render_template, request, redirect, url_for, flash,session,abort
from models import *

@app_bp.route('/', methods=['GET', 'POST'])
def index():
    homes = Home.query.all()
    abouts = About.query.all()
    
    skills = Skills.query.all()
    odd_skills = [skill for i, skill in enumerate(skills) if i % 2 == 0]
    even_skills = [skill for i, skill in enumerate(skills) if i % 2 != 0]
    
    educations = Education.query.all()
    experiences = Experience.query.all()
    categories = ProjectCategory.query.all()
    projects = Projects.query.all()
    contacts = Contact.query.all()
    return render_template('app/index.html', homes=homes, abouts=abouts, skills=skills, odd_skills=odd_skills, even_skills=even_skills, educations=educations, experiences=experiences, categories=categories, projects=projects, contacts=contacts)

@app_bp.route('/portfolio-details', methods=['GET', 'POST'])
def portfolio_details():
    return render_template('app/portfolio-details.html')