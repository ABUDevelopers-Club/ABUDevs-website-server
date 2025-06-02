# app/routes/students.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import Student
from app.schemas.student import StudentSchema
from app.utils.abudevs_id import generate_abudevs_id

students_bp = Blueprint('students', __name__)
student_schema = StudentSchema()

@students_bp.route('/register', methods=['POST'])
def register_student():
    data = request.get_json()
    
    # Validate input
    errors = student_schema.validate(data)
    if errors:
        return jsonify({'errors': errors}), 400

    # Generate unique serial (e.g., based on number of students)
    serial = Student.query.count() + 1
    abudevs_id = generate_abudevs_id(data['first_name'], data['student_id'], serial)

    # Create student
    student = Student(**data, abudevs_id=abudevs_id)
    db.session.add(student)
    db.session.commit()

    return jsonify({
        'message': 'Student registered successfully',
        'student': student_schema.dump(student)
    }), 201

