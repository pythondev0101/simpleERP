from datetime import datetime
from flask import redirect, render_template, url_for, request
from flask_login import current_user

from app import MONGO
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


@bp_main.route('/events')
def events():
    return render_template('main/event_locations.html')


@bp_main.route('/events/create', methods=['GET', 'POST'])
def create_event_location():
    if request.method == 'GET':
        return render_template('main/create_event_location.html')
    elif request.method == 'POST':
        form = request.form
        print(form)
        date_start = datetime.strptime(form.get('date_start'), '%Y-%m-%dT%H:%M')
        date_end = datetime.strptime(form.get('date_end'), '%Y-%m-%dT%H:%M')
        MONGO.db.events.insert_one({
            'name': form.get('name', ''),
            'description': form.get('description', ''),
            'address': form.get('address', ''),
            'date_start': date_start,
            'date_end': date_end,
            'lat': form.get('lat', 0),
            'lng': form.get('lng', 0)
        })

        return redirect(url_for('main.events'))
        