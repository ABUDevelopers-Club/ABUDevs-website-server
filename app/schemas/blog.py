# app/schemas/blog.py
from marshmallow import Schema, fields

class BlogSchema(Schema):
    id = fields.Int(dump_only=True)
    img_url = fields.Str()
    track = fields.Str(required=True)
    title = fields.Str(required=True)
    subtitle = fields.Str()
    body = fields.Str(required=True)
    author = fields.Str(required=True)
    author_position = fields.Str(required=True)
    date = fields.Date(dump_only=True)
    hashtags = fields.Str()
