# app/models/event.py
from app import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String(200))
    track = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    subtitle = db.Column(db.String(150))
    body = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    venue = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
