# app/models/student.py
from app import db
from datetime import datetime

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    student_id = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    current_level = db.Column(db.String(20), nullable=False)
    tech_experience_level = db.Column(db.String(50), nullable=False)
    area_of_interest = db.Column(db.String(200), nullable=False)
    reason_for_joining = db.Column(db.Text, nullable=False)
    abudevs_id = db.Column(db.String(50), unique=True, nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
