from src.models import db
import math
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
            total_pages = math.ceil(total/per_page)

            return characters, total_pages
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