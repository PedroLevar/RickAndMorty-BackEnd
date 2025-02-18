from flask import jsonify
from src.services.character_service import CharacterService

class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self, page, search_term):
        try:
            data = self.character_service.get_all_characters(page, search_term)
            return jsonify(data), 200
        except Exception:
            return jsonify({
                "error": "an error occurred."
            }), 500
        
    def get_character(self, id):
        try:
            data = self.character_service.get_character(id)
            if data:
                return jsonify(data), 200
            return jsonify({
                "error": "character not found."
            }), 404
        except Exception:
            return jsonify({
                "error": "An error occurred while searching for the character."
            }), 500