from werkzeug.exceptions import NotFound
from src.services.character_service import CharacterService
from src.utils.api_response import ApiResponse

class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self, page, search_term):
        try:
            data = self.character_service.get_all_characters(page, search_term)
            return ApiResponse.response(success=True, message="Personagens encontrados com Sucesso", data=data, status_code=200)
        except Exception:
            return ApiResponse.response(success=False, message="Erro ao encontrar Personagens", data=None, status_code=500)
        
    def get_character(self, id):
        try:
            data = self.character_service.get_character(id)
            return ApiResponse.response(success=True, message="Personagem encontrado com Sucesso", data=data, status_code=200)
        except NotFound:
            return ApiResponse.response(success=False, message="Personagem não encontrado", data=None, status_code=404)
        except Exception:
            return ApiResponse.response(success=False, message="Erro ao encontrar Personagem", data=None, status_code=500)
