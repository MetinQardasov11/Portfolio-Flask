from . import skills_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db, Contact
from .forms import SkillsForm

@skills_bp.route('/')
def index():
    from models import Skills
    skills = Skills.query.all()
    return render_template('admin/skills/index.html', skills=skills)


@skills_bp.route('/add', methods = ['GET', 'POST'])
def add():
    from models import Skills
    skillsForm = SkillsForm()
    if request.method == 'POST':
        skills = Skills(
            skill_name = skillsForm.skill_name.data,
            skill_percent = skillsForm.skill_percent.data
        )
        db.session.add(skills)
        db.session.commit()
        return redirect(url_for('admin.skills.index'))
    return render_template('admin/skills/add.html', skillsForm=skillsForm)


@skills_bp.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    from models import Skills
    skill = Skills.query.get(id)
    if request.method == 'POST':
        skill.skill_name = request.form['skill_name']
        skill.skill_percent = request.form['skill_percent']
        db.session.commit()
        return redirect(url_for('admin.skills.index'))
    return render_template('admin/skills/update.html', skill=skill)


@skills_bp.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    from models import Skills
    home = Skills.query.get(id)
    db.session.delete(home)
    db.session.commit()
    return redirect(url_for('admin.skills.index'))