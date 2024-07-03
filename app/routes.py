from . import app_bp
from flask import render_template, request, redirect, url_for, flash,session,abort
from models import *

@app_bp.route('/', methods=['GET', 'POST'])
def index():
    homes = Home.query.all()
    abouts = About.query.all()
    
    skills = Skills.query.all()
    odd_skills = [skill for i, skill in enumerate(skills) if i % 2 == 0]
    even_skills = [skill for i, skill in enumerate(skills) if i % 2 != 0]
    
    educations = Education.query.all()
    experiences = Experience.query.all()
    project_categories = ProjectCategory.query.all()
    projects = Projects.query.all()
    contacts = Contact.query.all()
    return render_template('app/index.html', homes=homes, abouts=abouts, skills=skills, odd_skills=odd_skills, even_skills=even_skills, educations=educations, experiences=experiences, project_categories=project_categories, projects=projects, contacts=contacts)

@app_bp.route('/portfolio-details', methods=['GET', 'POST'])
def portfolio_details():
    return render_template('app/portfolio-details.html')




# @app_bp.route('/register', methods = ['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         from models import Users,db
#         fullname = request.form.get('fullname')
#         email = request.form.get('email')
#         password = request.form.get('password')
#         confirm_password = request.form.get('confirm_password')
#         birthday = request.form.get('birthday')
#         gender = request.form.get('gender')
#         user=Users(fullname=fullname, email=email, password=password, confirm_password=confirm_password, birthday=birthday,gender=gender)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('app.login'))
#     return render_template('admin/register.html')


# @app_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         from models import Users, LoggedInUsers, db
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = Users.query.filter_by(email=email).first()
     
#         if user and user.password == password:
#             auth_user = LoggedInUsers(
#                 user_id=user.id, login_time=datetime.datetime.now(), is_logged_in=True)
#             session['user_id'] = user.id
#             session['is_logged_in'] = True
#             session['fullname'] = user.fullname
#             db.session.add(auth_user)
#             db.session.commit()
#             return redirect(url_for('admin.index'))
#     return render_template('admin/login.html')

# @app_bp.route('/logout', methods=['GET', 'POST'])
# def logout():
#     from models import LoggedInUsers, db
#     user_id = session.get('user_id')
#     all_logged_in_users = LoggedInUsers.query.filter_by(user_id=user_id).all()
#     for logged_in_user in all_logged_in_users:
#         logged_in_user.logout_time = datetime.datetime.now()
#         logged_in_user.is_logged_in = False
#     db.session.commit()
#     session.clear()
#     return redirect(url_for('app.login'))