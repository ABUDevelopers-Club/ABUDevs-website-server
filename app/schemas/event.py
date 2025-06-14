# app/schemas/event.py
from marshmallow import Schema, fields

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    img_url = fields.Str()
    track = fields.Str(required=True)
    title = fields.Str(required=True)
    subtitle = fields.Str()
    body = fields.Str(required=True)
    date = fields.Date(required=True)
    time = fields.Time(required=True)
    venue = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
