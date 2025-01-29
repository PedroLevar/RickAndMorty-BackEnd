from flask import jsonify
from src.services.character_service import CharacterService
from marshmallow.exceptions import ValidationError

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
        
    def create_character(self, data):
        try:
            data = self.character_service.create_character(data)
            return jsonify(data), 201
        
        except ValidationError as e:
            return jsonify({
                "erro": e.messages
            }), 400
        
        except Exception:
            return jsonify({
                "erro": "ocorreu um erro ao criar o personagem."
            }), 500
        
    def delete_character(self, id):
        try:
            success = self.character_service.delete_character(id)
            if success:
                return '', 204
            return jsonify({
                "erro": "personagem nao encontrado."
            }), 404
        except Exception as e:
            print(e)
            return jsonify({
                "erro": "ocorreu um erro ao deletar personagem."
            }), 500
        
    def update_character(self, id, data):
        try:
            character = self.character_service.update_character(id, data)
            return jsonify(character), 200
            
        except ValidationError as e:
                return jsonify({
                "erro": e.messages
            }), 400
        
        except Exception:
            return jsonify({
                "erro": "ocorreu um erro ao editar personagem."
            }), 500