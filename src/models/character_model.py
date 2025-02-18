from src.models import db, ma
from marshmallow import post_dump

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=True)
    species = db.Column(db.String(100), nullable=True)
    type = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    image = db.Column(db.String(255), nullable=True)

    origin_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)

    origin = db.relationship('Location', back_populates='character_origin', uselist=False, lazy=True, foreign_keys=[origin_id])
    location = db.relationship('Location', back_populates='character_location', uselist=False, lazy=True, foreign_keys=[location_id])
    episode = db.relationship('Episode', secondary='character_episode', back_populates='character')

    def __repr__(self):
        return f"<Character {self.name}>"

class CharacterOutputGetAll(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()
    image = ma.String()
    
class CharacterOutput(CharacterOutputGetAll):
    type = ma.String()
    gender = ma.String()
    origin = ma.Nested('LocationOutput', many=False)
    location = ma.Nested('LocationOutput', many=False)

class CharacterPaginationOutput(ma.Schema):
    data = ma.List(ma.Nested("CharacterOutputGetAll"))
    page = ma.Integer()
    total_items = ma.Integer()

    def calculate_total_pages(self, total_items):
        per_page = 20
        return (total_items // per_page) + (1 if total_items % per_page > 0 else 0)
    
    @post_dump
    def format_response(self, data, **kwargs):
        data["total_pages"] = self.calculate_total_pages(data["total_items"])
        data.pop("total_items")
        return data

character_output = CharacterOutput()  
character_pagination_output = CharacterPaginationOutput()