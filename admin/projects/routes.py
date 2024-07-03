from . import projects_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db, Contact
from helpers import *
from .forms import ProjectForm


@projects_bp.route('/', methods=['GET', 'POST'])
def index():
    from models import ProjectCategory, Projects
    project_categories = ProjectCategory.query.all()
    projects = Projects.query.all()
    return render_template('admin/projects/index.html', project_categories=project_categories, projects=projects)

@projects_bp.route('/add', methods=['GET', 'POST'])
def add():
    from models import Projects, ProjectCategory
    projectForm = ProjectForm()
    if request.method == 'POST':
        image = request.files['image']
        file_size = request.content_length
        extension = get_file_extension(image.filename)
        allowed_ext = ['jpg', 'jpeg', 'png', 'gif','JPG', 'JPEG', 'PNG', 'GIF']
        
        if extension in allowed_ext and file_size < 1024*1024*5:
            img_name = random_filename_for_projects(image.filename)
            save_file(image, 'app/static/assets/uploads', img_name)
        else:
            return redirect(url_for('admin.projects.add'))
        
        project = Projects(
            name = projectForm.name.data,
            image = img_name,
            link = projectForm.link.data,
            category_id = request.form['category_id'],
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('admin.projects.index'))
    projects = Projects.query.all()
    categories = ProjectCategory.query.all()
    return render_template('admin/projects/add.html', projectForm=projectForm, projects=projects, categories=categories)


@projects_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    from models import ProjectCategory, Projects
    project = Projects.query.get(id)
    categories = ProjectCategory.query.all()
    get_name_for_delete = project.image
    if request.method == 'POST':
        image = request.files['image']
        new_name = random_filename_for_projects(image.filename)
        save_file(image, 'app/static/assets/uploads', new_name)
        project.name = request.form['name']
        project.image = new_name
        project.link = request.form['link']
        project.category_id = request.form['category_id']
        db.session.commit()
        delete_file_from_folder(get_name_for_delete, 'app/static/assets/uploads')
        return redirect(url_for('admin.projects.index'))
    return render_template('admin/projects/update.html', project=project, categories=categories)


@projects_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    from models import Projects
    project = Projects.query.get(id)
    file_name_for_delete= project.image
    delete_file_from_folder(file_name_for_delete, 'app/static/assets/uploads')
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('admin.projects.index'))