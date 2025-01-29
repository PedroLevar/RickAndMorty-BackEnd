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
