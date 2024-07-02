from flask import Blueprint

skills_bp = Blueprint('skills', __name__, url_prefix='/skills', template_folder='templates', static_folder='static')

from . import routes