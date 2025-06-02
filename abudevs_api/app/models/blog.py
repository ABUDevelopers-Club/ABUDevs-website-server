# app/models/blog.py
from app import db
from datetime import datetime

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    subtitle = db.Column(db.String(150))
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    author_position = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    hashtags = db.Column(db.String(200))
