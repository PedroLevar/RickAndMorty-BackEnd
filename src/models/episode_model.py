from src.models import db, ma
from marshmallow import validate

class Episode(db.Model):
    __tablename__ = 'episode'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    air_date = db.Column(db.String(50), nullable=True)
    episode = db.Column(db.String(20), nullable=True)

    character = db.relationship('Character', secondary='character_episode', back_populates='episode')

    def __repr__(self):
        return f"<Episode {self.name}>"

class EpisodeOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.String()
    episode = ma.String()

episode_output = EpisodeOutput()
episodes_output = EpisodeOutput(many=True)