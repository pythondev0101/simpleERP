from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user
from werkzeug.urls import url_parse
from app.auth import bp_auth
from app.auth.models import User



@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user: User = User.find_by_username(username)
        
        if not user:
            flash('Invalid username or password','error')
            return redirect(url_for('auth.login'))

        if user is None or not user.check_password(password):
            flash('Invalid username or password','error')
            return redirect(url_for('auth.login'))

        login_user(user, remember=False)
        
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.dashboard')
        return redirect(next_page)
