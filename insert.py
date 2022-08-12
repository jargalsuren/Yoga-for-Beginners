#import required modules
# import sqlalchemy
# from sqlalchemy import create_engine, Column, Text,Integer,ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import  sessionmaker
# from sqlalchemy.sql.sqltypes import Boolean
# from datetime import date

from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from web import db
from web.models import SavedVideo, Video
# from .models import *

#fictitious Video data: id, name, channel_name, length, youtube_video_id, thumbnail
videos = [
    [1, "Flex & Stretch","FitOn", 15, "zwoVcrdmLOE", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3620&q=80"],
    [2, "Feel Good Now","Yoga with Dodie", 30, "sTANio_2E0Q", "https://images.unsplash.com/photo-1575052814086-f385e2e2ad1b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=800"],
    [3, "Yoga for Beginnerss", "Yogi Adrienne", 10, "AB3Y-4a3ZrU", "https://images.unsplash.com/photo-1506126613408-eca07ce68773?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1399&q=80"],
    [4, "Yoga to Breathe","Boho Beautiful Yoga", 30, "6zzeSJxJS4s", "https://images.unsplash.com/photo-1552196563-55cd4e45efb3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2226&q=80"],
    [5, "Everyday Yoga","Yoga with Bird", 17, "zwoVcrdmLOE", "https://images.unsplash.com/photo-1562088287-bde35a1ea917?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1364&q=80"],
    [6, "Stress Relief Yoga flow","Yogi Rachel", 20, "mPYA6_rKdtU", "https://images.unsplash.com/photo-1552286450-4a669f880062?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1760&q=80"]
]

saved_videos =[
    [1,1,1],
    [2,2,1],
    [3,6,1]
]


#Populate all mock data
for video in videos:
    db.session.add(Video(id=video[0], name = video[1], channel_name=video[2], length=video[3], youtube_video_id =video[4], thumbnail = video[5]))
    
for video in saved_videos:
    db.session.add(SavedVideo(id=video[0], video_id=video[1], user_id=video[2]))

db.session.commit()