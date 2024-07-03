from . import project_category_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db
from .forms import ProjectCategoryForm

@project_category_bp.route('/', methods=['GET', 'POST'])
def index():
    from models import ProjectCategory
    categories = ProjectCategory.query.all()
    return render_template('admin/project_category/index.html', categories=categories)

@project_category_bp.route('/add', methods=['GET', 'POST'])
def add():
    from models import ProjectCategory
    categoryForm = ProjectCategoryForm()
    if request.method == 'POST':
        category = ProjectCategory(
            name = categoryForm.name.data,
        )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('admin.project_category.index'))
    return render_template('admin/project_category/add.html', categoryForm=categoryForm)

@project_category_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    from models import ProjectCategory
    category = ProjectCategory.query.get(id)
    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        return redirect(url_for('admin.project_category.index'))
    return render_template('admin/project_category/update.html', category=category)

@project_category_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    from models import ProjectCategory
    category = ProjectCategory.query.get(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('admin.project_category.index'))