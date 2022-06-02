from unicodedata import name
from marshmallow import fields

from app.ext import ma

class CrewSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    ship = fields.String()
    status = fields.String()
    members = fields.Nested('CharacterSchema', many=True)

class CharacterSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    status = fields.String()
    origin = fields.String()
    crew_id = fields.String()
    devil_fruit_id = fields.Nested('DevilFruitsSchema', many=False)

class DevilFruitSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    status = fields.String()