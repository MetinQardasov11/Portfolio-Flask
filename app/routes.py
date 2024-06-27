from . import app_bp
from flask import render_template, request, redirect, url_for, flash,session,abort
from models import *

@app_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('app/index.html')