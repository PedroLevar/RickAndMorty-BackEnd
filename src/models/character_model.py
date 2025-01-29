from src.models import db, ma
from marshmallow import validate

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=True)
    species = db.Column(db.String(100), nullable=True)

def __repr__(self):
    return f"<Character {self.name})>"

class CharacterInput(ma.Schema): 
    name = ma.String(required=True, validate=validate.Length(min=3, max=100))
    status = ma.String(required=False, validate=validate.Length(max=50), allow_none=True)
    species = ma.String(required=False, validate=validate.Length(max=100), allow_none=True)

class CharacterInputUpdate(ma.Schema):
    name = ma.String(required=False, validate=validate.Length(min=3, max=100))
    status = ma.String(required=False, validate=validate.Length(max=50), allow_none=True)
    species = ma.String(required=False, validate=validate.Length(max=100), allow_none=True)

class CharacterOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()

character_input = CharacterInput()
character_input_update = CharacterInputUpdate()
character_output = CharacterOutput()
characters_output = CharacterOutput (many=True)