from src.repositories.character_repository import CharacterRepository
from src.models.character_model import character_output, character_pagination_output
from werkzeug.exceptions import NotFound

class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()

    def get_all_characters(self, page, search_term):
        characters, total_pages = self.character_repository.get_all_characters(page, search_term)
        data = {
            "characters": characters,
            "page": page,
            "total_pages": total_pages
        }
        return character_pagination_output.dump(data)
    
    def get_character(self, id):
        character = self.character_repository.get_character(id)
        if character is None:
            raise NotFound(f"Character with ID {id} not found.")
        
        return character_output.dump(character)
