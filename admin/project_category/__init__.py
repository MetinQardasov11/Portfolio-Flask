from flask import Blueprint

project_category_bp = Blueprint('project_category', __name__, url_prefix='/project_category', template_folder='templates', static_folder='static')

from . import routes