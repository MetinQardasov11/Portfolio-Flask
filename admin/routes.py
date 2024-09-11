from . import admin_bp
from flask import render_template, session, redirect, request, url_for, jsonify
from datetime import datetime
from models import *
from functools import wraps
from flask import session, redirect, url_for
from werkzeug.security import check_password_hash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('admin.login'))  # Redirect to the login page if user_id is not in session
        return f(*args, **kwargs)
    return decorated_function


@admin_bp.route('/')
# @login_required
def index():
    return render_template('admin/index.html')

@admin_bp.route('/login', methods=['GET', 'POST'])
# @login_required
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = Users.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            user.is_logged_in = True
            db.session.commit()
            return redirect(url_for('admin.index'))
        else:
            return render_template('admin/login.html')
    return render_template('admin/login.html')
    
@admin_bp.route('/logout', methods=['GET', 'POST'])
# @login_required
def logout():
    if 'user_id' in session:
        user = Users.query.get(session['user_id'])
        user.is_logged_in = False
        db.session.commit()
        session.pop('user_id', None)
    
    return redirect(url_for('admin.login'))