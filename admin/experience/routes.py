from . import experience_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db
from .forms import ExperienceForm
from flask_ckeditor import CKEditor

@experience_bp.route('/')
def index():
    from models import Experience
    experiences = Experience.query.all()
    return render_template('admin/experience/index.html', experiences=experiences)


@experience_bp.route('/add', methods = ['GET', 'POST'])
def add():
    from models import Experience
    experienceForm = ExperienceForm()
    if request.method == 'POST':
        experience = Experience(
            job_title = experienceForm.job_title.data,
            start_date = experienceForm.start_date.data,
            end_date = experienceForm.end_date.data,
            company_name = experienceForm.company_name.data,
            description = experienceForm.description.data,
        )
        db.session.add(experience)
        db.session.commit()
        return redirect(url_for('admin.experience.index'))
    return render_template('admin/experience/add.html', experienceForm=experienceForm)

@experience_bp.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    from models import Experience
    experience = Experience.query.get(id)
    if request.method == 'POST':
        experience.job_title = request.form['job_title']
        experience.start_date = request.form['start_date']
        experience.end_date = request.form['end_date']
        experience.company_name = request.form['company_name']
        experience.description = request.form['description']
        db.session.commit()
        return redirect(url_for('admin.experience.index'))
    return render_template('admin/experience/update.html', experience=experience)


@experience_bp.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    from models import Experience
    experience = Experience.query.get(id)
    db.session.delete(experience)
    db.session.commit()
    return redirect(url_for('admin.experience.index'))