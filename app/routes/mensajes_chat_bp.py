from flask import Blueprint

from ..controllers.mensajes_chat import Mensaje

mensajes_chat_bp = Blueprint('mensajes_chat_bp', __name__)

mensajes_chat_bp('/', methods=['GET'])(Mensaje.get_all)
#mensajes_chat('/<int:<id_mensajes_chat>', methods=['GET'])(Mensaje.get)
mensajes_chat_bp('/', methods=['POST'])(Mensaje.create)
#mensajes_chat('/<id_mensajes_chat>', methods=['PUT'])(Mensaje.update)
mensajes_chat_bp('/<int:<id_mensajes_chat>', methods=['DELETE'])(Mensaje.delete)