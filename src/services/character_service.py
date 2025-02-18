from src.repositories.character_repository import CharacterRepository
from src.models.character_model import character_output, character_pagination_output

class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()

    def get_all_characters(self, page, search_term):
        characters, total = self.character_repository.get_all_characters(page, search_term)
        data = {
            "data": characters,
            "page": page,
            "total_items": total
        }
        return character_pagination_output.dump(data)
    
    def get_character(self, id):
        character = self.character_repository.get_character(id)
        if not character:
            return None
        data = character_output.dump(character)
        return {
            "data": data
        }
    