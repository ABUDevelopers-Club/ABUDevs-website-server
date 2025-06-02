# app/routes/blogs.py
from flask import Blueprint

blogs_bp = Blueprint('blogs', __name__)

@blogs_bp.route('/')
def index():
    return {'message': 'Blog route works'}

