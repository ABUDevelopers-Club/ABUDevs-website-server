# app/routes/students.py
from flask import Blueprint

students_bp = Blueprint('students', __name__)

@students_bp.route('/')
def index():
    return {'message': 'Student route works'}
