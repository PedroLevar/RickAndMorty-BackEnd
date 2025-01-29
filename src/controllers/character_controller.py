from flask import jsonify
from src.services.character_service import CharacterService

class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self):
        try:
            data = self.character_service.get_all_characters()
            return jsonify(data), 200
        except Exception:
            return jsonify({
                "erro": "ocorreu um erro."
            }), 500
        
    def get_character(self, id):
        try:
            data = self.character_service.get_character(id)
            if data:
                return jsonify(data), 200
            return jsonify({
                "erro": "personagem nao encontrado."
            }), 404
        except Exception:
            return jsonify({
                "erro": "ocorreu um erro ao buscar o personagem."
            }), 500