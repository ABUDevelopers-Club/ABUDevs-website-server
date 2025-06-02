# app/schemas/student.py
from marshmallow import Schema, fields, validate

class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True, validate=validate.Length(min=2))
    last_name = fields.Str(required=True, validate=validate.Length(min=2))
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True)
    student_id = fields.Str(required=True)
    department = fields.Str(required=True)
    current_level = fields.Str(required=True)
    tech_experience_level = fields.Str(required=True)
    area_of_interest = fields.Str(required=True)
    reason_for_joining = fields.Str(required=True)
    abudevs_id = fields.Str(dump_only=True)
    registered_at = fields.DateTime(dump_only=True)
