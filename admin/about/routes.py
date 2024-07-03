from . import about_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db, Contact
from helpers import *
from flask_ckeditor import CKEditor
from .forms import AboutForm

@about_bp.route('/')
def index():
    from models import About
    abouts = About.query.all()
    return render_template('admin/about/index.html', abouts=abouts)


@about_bp.route('/add', methods = ['GET', 'POST'])
def add():
    from models import About
    aboutForm = AboutForm()
    if request.method == 'POST':
        image = request.files['image']
        file_size = request.content_length
        extension = get_file_extension(image.filename)
        allowed_ext = ['jpg', 'jpeg', 'png', 'gif','JPG', 'JPEG', 'PNG', 'GIF']
        
        if extension in allowed_ext and file_size < 1024*1024*5:
            img_name = random_filename_for_about(image.filename)
            save_file(image, 'app/static/assets/uploads', img_name)
        else:
            return redirect(url_for('admin.about.add'))
        
        about = About(
            image = img_name,
            job = aboutForm.job.data,
            birthday = aboutForm.birthday.data,
            website = aboutForm.website.data,
            phone = aboutForm.phone.data,
            city = aboutForm.city.data,
            age = aboutForm.age.data,
            email = aboutForm.email.data,
            description = aboutForm.description.data, 
        )
        db.session.add(about)
        db.session.commit()
        return redirect(url_for('admin.about.index'))
    return render_template('admin/about/add.html', aboutForm=aboutForm)


@about_bp.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    from models import About
    about = About.query.get(id)
    get_name_for_delete = about.image
    if request.method == 'POST':
        image = request.files['image']
        new_name = random_filename_for_about(image.filename)
        save_file(image, 'app/static/assets/uploads', new_name)
        about.image = new_name
        about.job = request.form['job']
        about.birthday = request.form['birthday']
        about.website = request.form['website']
        about.phone = request.form['phone']
        about.city = request.form['city']
        about.age = request.form['age']
        about.email = request.form['email']
        about.description = request.form['description']
        
        db.session.commit()
        delete_file_from_folder(get_name_for_delete, 'app/static/assets/uploads/')
        return redirect(url_for('admin.about.index'))
    return render_template('admin/about/update.html', about=about)


@about_bp.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    from models import About
    about = About.query.get(id)
    file_name_for_delete= about.image
    delete_file_from_folder(file_name_for_delete, 'app/static/assets/uploads')
    db.session.delete(about)
    db.session.commit()
    return redirect(url_for('admin.about.index'))