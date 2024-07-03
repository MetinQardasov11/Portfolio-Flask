from . import home_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db
from .forms import HomeForm

@home_bp.route('/')
def index():
    from models import Home
    homes = Home.query.all()
    return render_template('admin/home/index.html', homes=homes)


@home_bp.route('/add', methods = ['GET', 'POST'])
def add():
    from models import Home
    homeForm = HomeForm()
    if request.method == 'POST':
        home = Home(
            full_name = homeForm.full_name.data,
            content = homeForm.content.data,
            github_link = homeForm.github_link.data,
            linkedin_link = homeForm.linkedin_link.data,
            facebook_link = homeForm.facebook_link.data,
            email = homeForm.email.data,
        )
        db.session.add(home)
        db.session.commit()
        return redirect(url_for('admin.home.index'))
    return render_template('admin/home/add.html', homeForm=homeForm)


@home_bp.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    from models import Home
    home = Home.query.get(id)
    if request.method == 'POST':
        home.full_name = request.form['full_name']
        home.content = request.form['content']
        home.github_link = request.form['github_link']
        home.linkedin_link = request.form['linkedin_link']
        home.facebook_link = request.form['facebook_link']
        home.email = request.form['email']
        db.session.commit()
        return redirect(url_for('admin.home.index'))
    return render_template('admin/home/update.html', home=home)


@home_bp.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    from models import Home
    home = Home.query.get(id)
    db.session.delete(home)
    db.session.commit()
    return redirect(url_for('admin.home.index'))