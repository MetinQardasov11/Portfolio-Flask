from flask import Blueprint

education_bp = Blueprint('education', __name__, url_prefix='/education', template_folder='templates', static_folder='static')

from . import routes