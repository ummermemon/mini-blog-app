from functools import wraps
from flask import session,redirect,url_for
from app.models.user import User
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated

def logout_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' in session:
            return redirect(url_for('panel.dashboard'))
        return f(*args, **kwargs)
    return decorated