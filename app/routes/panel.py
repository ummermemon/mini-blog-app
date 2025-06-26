from flask import Blueprint
from app.middlewares.auth import login_required
panel = Blueprint('panel', __name__, url_prefix='/panel')

@panel.route('/')
@login_required
def dashboard():
    return 'panel dashboard'