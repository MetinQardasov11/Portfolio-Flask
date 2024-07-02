from flask import Blueprint

experience_bp = Blueprint('experience', __name__, url_prefix='/experience', template_folder='templates', static_folder='static')

from . import routes