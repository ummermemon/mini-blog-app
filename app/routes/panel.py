from flask import Blueprint

panel = Blueprint('panel', __name__, url_prefix='/panel')

@panel.route('/')
def dashboard():
    return 'panel dashboard'