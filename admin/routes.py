from . import admin_bp
from flask import render_template, session, redirect, request
from flask import url_for
from datetime import datetime
from models import *
from functools import wraps


@admin_bp.route('/')
def index():
    return render_template('admin/index.html')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('admin/login.html')