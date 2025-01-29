from flask import Blueprint, request
from src.controllers.character_controller import CharacterController

character_bp = Blueprint('character_bp', __name__)
character_controller = CharacterController()

@character_bp.route('/', methods=['GET'])
def get_all_characters():
    return character_controller.get_all_characters()

@character_bp.route('/<int:id>', methods=['GET'])
def get_character(id):
    return character_controller.get_character(id)

@character_bp.route('/', methods=['POST'])
def create_character():
    data = request.get_json()
    return character_controller.create_character(data)

@character_bp.route('/<int:id>', methods=['DELETE'])
def delete_character(id):
    return character_controller.delete_character(id)

@character_bp.route('/<int:id', methods=['PATCH'])
def update_character(id):
    data = request.get_json()
    return character_controller.update_character(id, data)
