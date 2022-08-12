from flask_sqlalchemy import SQLAlchemy
from click import password_option
from flask import Flask
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from web import app, db, bcrypt
from datetime import datetime
from web.forms import register_form, login_form
from web.queries import *

# from flask_login import login_manager


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None
        
@app.route('/')
def index():
    videos  = get_all_videos()
    return render_template('index.html', videos=videos)

@app.route('/users')
def users():
    users = get_all_users()
    return render_template('users.html', users=users)

@app.route('/')
def home_page():
    return render_template('login.html')

@app.route('/browse')
def browse_page():
    videos  = get_all_videos()
    return render_template('browse.html', videos=videos)

@app.route('/courses')
def courses_page():
    # courses = get_all_courses()
    return render_template('courses.html')

@app.route('/watch/<id>')
def watch_page(id):
    video  = get_video_by_id(id)
    return render_template('watch.html', video=video)

@app.route('/profile')
@login_required
def profile_page():
        user_id= current_user.get_id()
        saved_videos = get_all_videos_saved_by_user(user_id)
        return render_template('profile.html', saved_videos=saved_videos)

@app.route('/fetch_data', methods=['POST', 'GET'])
def FetchData():
    if request.method=="POST":
        user = request.form['nm']
        password = request.form['pw']
        return redirect(url_for('Success', name=user, passwrd=password))
    else:
        user = request.args.get('nm')
        password = request.args.get('pw')
        return redirect(url_for('Success', name=user, passwrd=password))

@app.route("/register",methods=['GET','POST'])
def register():
    form = register_form()
    if form.validate_on_submit():
        # storing hashed password value
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # update db
        db.session.add(user)
        db.session.commit()
        # alert
        flash(f'Your account has been created, {form.username.data}!', category='success')
        return redirect(url_for('browse_page'))
    return render_template('register.html', title="Register", form=form)

# login
@app.route("/login",methods=['GET','POST'])
def login():
    # check authentication
    if current_user.is_authenticated: return redirect(url_for('home'))
    form = login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # hashed password check
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Logged in successfully!', category='success')
            login_user(user)
            return redirect(url_for('browse_page'))
        else: flash(f'Please login again!', category='error')
    return render_template('login.html', title="Login", form=form)

# logout user
@app.route("/logout")
def logout():
    flash('Logged out successfully!', category='success')
    logout_user()
    return render_template('index.html')