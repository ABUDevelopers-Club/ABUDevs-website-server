# app/routes/events.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Event, User
from app import db
from app.schemas.event import EventSchema
from functools import wraps
from marshmallow import ValidationError
from app.models.event import Event

events_bp = Blueprint('events', __name__)
event_schema = EventSchema()
events_schema = EventSchema(many=True)

# Admin check decorator
def require_admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        identity = get_jwt_identity()
        user_id = identity.get('id') if isinstance(identity, dict) else None
        user = User.query.get(user_id)
        if not user or not user.is_admin:
            return jsonify({'error': 'Admins only'}), 403
        return fn(*args, **kwargs)
    return wrapper


@events_bp.route('/events', methods=['POST'])
@jwt_required()
@require_admin
def create_event():
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message": "No input data provided"}), 400

    try:
        # Marshmallow does the validation AND conversion here
        data = event_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    event = Event(**data)  # ✅ Now data["date"] is a datetime.date object
    db.session.add(event)
    db.session.commit()

    return jsonify(event_schema.dump(event)), 201


# Get all events (public)
@events_bp.route('/events', methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.date.desc(), Event.time.desc()).all()
    return jsonify(events_schema.dump(events)), 200

# Get single event (public)
@events_bp.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify(event_schema.dump(event)), 200

# Update event (admin only)
@events_bp.route('/events/<int:event_id>', methods=['PUT'])
@jwt_required()
@require_admin
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    data = request.get_json()
    errors = event_schema.validate(data, partial=True)
    if errors:
        return jsonify({'errors': errors}), 400

    for key, value in data.items():
        setattr(event, key, value)

    db.session.commit()
    return jsonify({'message': 'Event updated successfully', 'event': event_schema.dump(event)}), 200

# Delete event (admin only)
@events_bp.route('/events/<int:event_id>', methods=['DELETE'])
@jwt_required()
@require_admin
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Event deleted successfully'}), 200
