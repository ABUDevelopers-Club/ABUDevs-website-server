# app/routes/events.py
from flask import Blueprint

events_bp = Blueprint('events', __name__)

@events_bp.route('/')
def index():
    return {'message': 'Events route works'}

