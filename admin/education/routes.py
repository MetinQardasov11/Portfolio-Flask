from . import education_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db
from .forms import EducationForm
from flask_ckeditor import CKEditor

@education_bp.route('/')
def index():
    from models import Education
    educations = Education.query.all()
    return render_template('admin/education/index.html', educations=educations)


@education_bp.route('/add', methods = ['GET', 'POST'])
def add():
    from models import Education
    educationForm = EducationForm()
    if request.method == 'POST':
        education = Education(
            speciality = educationForm.speciality.data,
            start_date = educationForm.start_date.data,
            end_date = educationForm.end_date.data,
            university = educationForm.university.data,
            description = educationForm.description.data,
        )
        db.session.add(education)
        db.session.commit()
        return redirect(url_for('admin.education.index'))
    return render_template('admin/education/add.html', educationForm=educationForm)


@education_bp.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    from models import Education
    education = Education.query.get(id)
    if request.method == 'POST':
        education.speciality = request.form['speciality']
        education.start_date = request.form['start_date']
        education.end_date = request.form['end_date']
        education.university = request.form['university']
        education.description = request.form['description']
        db.session.commit()
        return redirect(url_for('admin.education.index'))
    return render_template('admin/education/update.html', education=education)


@education_bp.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    from models import Education
    education = Education.query.get(id)
    db.session.delete(education)
    db.session.commit()
    return redirect(url_for('admin.education.index'))