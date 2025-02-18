from src.models import db
from src.models.character_model import Character

class CharacterRepository:

    def get_all_characters(self, page, search_term):
        try:
            per_page = 20
            offset = (page - 1) * per_page

            query = Character.query

            if search_term:
                query = query.filter(Character.name.ilike(f"%{search_term}%"))

            characters = query.limit(per_page).offset(offset).all()
            total = query.count()

            return characters, total
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