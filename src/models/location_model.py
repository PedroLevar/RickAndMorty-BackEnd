from src.models import db, ma
from marshmallow import validate

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    dimension = db.Column(db.String(100), nullable=True)
    residents_count = db.Column(db.Integer, nullable=True)

    character_origin = db.relationship('Character', back_populates='origin', uselist=True, lazy=True, foreign_keys='Character.origin_id')
    character_location = db.relationship('Character', back_populates='location', uselist=True, lazy=True, foreign_keys='Character.location_id')

    def __repr__(self):
        return f"<Location {self.name}>"
    
class LocationOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    type = ma.String()
    dimension = ma.String()
    residents_count = ma.Integer()

location_output = LocationOutput()
locations_output = LocationOutput(many=True)