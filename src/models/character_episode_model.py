from src.models import db

class CharacterEpisode(db.Model):
    __tablename__ = 'character_episode'

    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)

    def __repr__(self):
        return f"<CharacterEpisode episode_id={self.episode_id} character_id={self.character_id}>"
    