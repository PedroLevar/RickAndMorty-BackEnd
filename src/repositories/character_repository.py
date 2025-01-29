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

    def create_character(self, character):
        try:
            db.session.add(character)
            db.session.commit()
            return character
        except Exception:
            db.session.rollback()
            raise

    def delete_character(self, character):
        try:
            db.session.delete(character)
            db.session.commit()
            return character
        except Exception:
            db.session.rollback()
            raise

    def update_character(self, character, data):
        try:
            for key, value in data.items():
                setattr(character, key, value)
            db.session.commit()
            return character
        except Exception:
            db.session.rollback()
            raise
