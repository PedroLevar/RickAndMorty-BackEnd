from src.models import db
from src.models.character_model import Character

class CharacterRepository:

    def get_all_characters(self):
        try:
            characters = Character.query.all()
            return characters
        except Exception:
            db.session.rollback()
            raise

    def get_character(self, id):
        try:
            character = db.session.get(Character, id)
            return character
        except Exception:
            db.session.rollback()
            raise