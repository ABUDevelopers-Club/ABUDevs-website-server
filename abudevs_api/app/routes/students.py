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

    # Check for existing email
    existing_student = Student.query.filter_by(email=data['email']).first()
    if existing_student:
        return jsonify({'error': 'Email already registered'}), 409

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


@students_bp.route('/', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    return jsonify(student_schema.dump(students, many=True)), 200

@students_bp.route('/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(student_schema.dump(student)), 200


@students_bp.route('/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    data = request.get_json()
    errors = student_schema.validate(data, partial=True)
    if errors:
        return jsonify({'errors': errors}), 400

    for key, value in data.items():
        setattr(student, key, value)

    db.session.commit()
    return jsonify({'message': 'Student updated', 'student': student_schema.dump(student)}), 200

@students_bp.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'}), 200

