from flask import redirect, render_template, url_for
from flask_login import current_user
from . import bp_main


@bp_main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    else:
        return redirect(url_for('auth.login'))
    
    
@bp_main.route('/dashboard')
def dashboard():
    return render_template('main/dashboard.html')