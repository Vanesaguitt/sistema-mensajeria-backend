from flask import Blueprint

from ..controllers.servidor_u_s import Servidor

servidor_u_s_bp = Blueprint('servidor_u_s', __name__)

servidor_u_s_bp('/', methods=['GET'])(Servidor.get_all)
#servidor_u_s_bp('/<int:<id_servidor_u_s>', methods=['GET'])(Servidor.get)
servidor_u_s_bp('/', methods=['POST'])(Servidor.create)
#servidor_u_s_bp('/<id_servidor_u_s>', methods=['PUT'])(Servidor.update)
servidor_u_s_bp('/<int:<id_servidor_u_s>', methods=['DELETE'])(Servidor.delete)