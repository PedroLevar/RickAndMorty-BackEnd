from src.models import db, ma

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

    @property
    def last_seen(self):
        """Retorna o último episódio em que o personagem apareceu"""
        return self.episode[-1].air_date

    def __repr__(self):
        return f"<Character {self.name}>"

# API Schemas
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
    last_seen = ma.String(attribute="last_seen")

class CharacterPaginationOutput(ma.Schema):
    characters = ma.List(ma.Nested("CharacterOutputGetAll"))
    page = ma.Integer()
    total_pages = ma.Integer()

character_output = CharacterOutput()  
character_pagination_output = CharacterPaginationOutput()