from flask import Blueprint

about_bp = Blueprint('about', __name__, url_prefix='/about', template_folder='templates', static_folder='static')

from . import routes