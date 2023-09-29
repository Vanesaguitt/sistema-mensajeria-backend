from flask import Blueprint

from ..controllers.mensajes_chat import MensajesController

mensajes_chat_bp = Blueprint('mensajes_chat_bp', __name__)

mensajes_chat_bp.route('/<string:sala>/messages', methods=['GET'])(MensajesController.get_mensajes_by_sala)
mensajes_chat_bp.route('/messages', methods=['POST'])(MensajesController.create_mensaje_chat)