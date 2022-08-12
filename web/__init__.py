from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

"""
I'm making changes to Flask arguments because it will allow referencing static files in an easier way
in practice, it will look like this -
<link rel="stylesheet" type="text/css" href="/css/file_name.css">
"""

#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# app.secret_key = os.getenv('SECRET_KEY')

#create an SQLite DB called ap.db
app = Flask(__name__, static_url_path='', static_folder='static', instance_relative_config=True)
app.config['SECRET_KEY'] = '**********'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#authentication
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from web import models,routes

db.create_all()
db.session.commit()