from .home import home_bp
from .about import about_bp
from .skills import skills_bp
from .education import education_bp
from .experience import experience_bp
from .project_category import project_category_bp
from .projects import projects_bp
from .contact import contact_bp
from flask import Blueprint

admin_bp = Blueprint('admin', __name__,url_prefix='/admin', template_folder='templates', static_folder='static')

from . import routes

admin_bp.register_blueprint(home_bp)
admin_bp.register_blueprint(about_bp)
admin_bp.register_blueprint(skills_bp)
admin_bp.register_blueprint(education_bp)
admin_bp.register_blueprint(experience_bp)
admin_bp.register_blueprint(project_category_bp)
admin_bp.register_blueprint(projects_bp)
admin_bp.register_blueprint(contact_bp)