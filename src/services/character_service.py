from src.repositories.character_repository import CharacterRepository
from src.models.character_model import character_output, characters_output, character_input, character_input_update, Character

class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()

    def get_all_characters(self):
        characters = self.character_repository.get_all_characters()
        data = characters_output.dump(characters)
        return {
            "data": data
        }
    
    def get_character(self, id):
        character = self.character_repository.get_character(id)
        if not character:
            return None
        data = character_output.dump(character)
        return {
            "data": data
        }
    
    def create_character(self, data):
        validated_data = character_input.load(data)

        character = Character(
            name=validated_data['name'],
            status=validated_data['status'],
            species=validated_data['species']
        )

        character = self.character_repository.create_character(character)

        data = character_output.dump(character)

        return {
            "data": data
        }
    
    def delete_character(self, id):
        character = self.character_repository.get_character(id)
        if not character:
            return None
        
        self.character_repository.delete_character(character)

        return {
            "data": None
        }
    
    def update_character(self, id, data):
        validated_data = character_input_update.load(data)

        character = self.character_repository.get_character(id)
        if not character:
            return None
        
        updated_character = self.character_repository.update_character(character, validated_data)

        data = character_output.dump(updated_character)

        return {
            "data": data
        }