from web import db, login_manager
from flask_login import UserMixin

# User db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(16),unique=True,nullable=False)
    email = db.Column(db.String(96),unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)

#Creating a database model for storing videos 
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    channel_name = db.Column(db.String(200), unique=True, nullable=False)
    length = db.Column(db.Integer)
    youtube_video_id = db.Column(db.String(100), nullable=False)
    thumbnail = db.Column(db.String(500), nullable=False)
    
    def __repr__(self):
        return '<Video %r>' % self.id

class SavedVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    video = db.relationship('Video', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Video %r>' % self.id

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(200), nullable=False)
    chapter1_name = db.Column(db.String(200), nullable=False)
    total_chapters = db.Column(db.Integer)

    def __repr__(self):
        return '<Video %r>' % self.id

