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



@bp_main.route('/users')
def users():
    return render_template('main/users.html')


@bp_main.route('/event-locations')
def event_locations():
    return render_template('main/event_locations.html')


@bp_main.route('/event-location/create')
def create_event_location():
    return render_template('main/create_event_location.html')