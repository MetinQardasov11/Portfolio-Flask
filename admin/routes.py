from . import admin_bp
from flask import render_template,session,redirect,url_for, session
from functools import wraps


@admin_bp.route('/')
def index():
    return render_template('admin/index.html')
