# app/routes/blogs.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Blog, User
from app.schemas.blog import BlogSchema
from app import db

blogs_bp = Blueprint('blogs', __name__)
blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)

def admin_required():
    identity = get_jwt_identity()
    
    if not identity or not isinstance(identity, dict):
        return jsonify({'error': 'Invalid token structure'}), 401

    user_id = identity.get('id')
    if not user_id:
        return jsonify({'error': 'User ID not found in token'}), 401

    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return jsonify({'error': 'Admins only'}), 403

    return None  # if valid


# Create blog (admin only)
@blogs_bp.route('/blogs', methods=['POST'])
@jwt_required()
def create_blog():
    error = admin_required()
    if error: return error

    data = request.get_json()
    errors = blog_schema.validate(data)
    if errors:
        return jsonify({'errors': errors}), 400

    blog = Blog(**data)
    db.session.add(blog)
    db.session.commit()

    return jsonify({'message': 'Blog created', 'blog': blog_schema.dump(blog)}), 201

# Get all blogs (public)
@blogs_bp.route('/blogs', methods=['GET'])
def get_blogs():
    blogs = Blog.query.order_by(Blog.date.desc()).all()
    return jsonify({'blogs': blogs_schema.dump(blogs)}), 200

# Get one blog (public)
@blogs_bp.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return jsonify({'blog': blog_schema.dump(blog)}), 200

# Update blog (admin only)
@blogs_bp.route('/blogs/<int:blog_id>', methods=['PUT'])
@jwt_required()
def update_blog(blog_id):
    error = admin_required()
    if error: return error

    blog = Blog.query.get_or_404(blog_id)
    data = request.get_json()

    errors = blog_schema.validate(data, partial=True)
    if errors:
        return jsonify({'errors': errors}), 400

    for key, value in data.items():
        setattr(blog, key, value)

    db.session.commit()
    return jsonify({'message': 'Blog updated', 'blog': blog_schema.dump(blog)}), 200

# Delete blog (admin only)
@blogs_bp.route('/blogs/<int:blog_id>', methods=['DELETE'])
@jwt_required()
def delete_blog(blog_id):
    error = admin_required()
    if error: return error

    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return jsonify({'message': 'Blog deleted'}), 200

