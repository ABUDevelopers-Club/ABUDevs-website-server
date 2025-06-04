# app/routes/auth.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)
from app.models import User
from app import db
from datetime import timedelta
from functools import wraps

auth_bp = Blueprint('auth', __name__)

# ------------------------
# Admin Registration Route
# ------------------------
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 409

    user = User(username=username)
    user.set_password(password)
    user.is_admin = True  # Optional, ensure admin creation only
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Admin user registered successfully'}), 201

# ------------------------
# Admin Login Route
# ------------------------
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password'}), 401

    access_token = create_access_token(identity={'id': user.id, 'username': user.username, 'is_admin': user.is_admin}, expires_delta=timedelta(hours=1))
    return jsonify({'access_token': access_token}), 200

# ------------------------
# Get Current User Route
# ------------------------
@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    user_data = get_jwt_identity()
    return jsonify({'user': user_data}), 200

# ------------------------
# Admin-Only Decorator
# ------------------------
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user = get_jwt_identity()
        if not user.get('is_admin'):
            return jsonify({'error': 'Admin access required'}), 403
        return fn(*args, **kwargs)
    return wrapper
