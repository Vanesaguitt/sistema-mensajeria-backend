from flask import Blueprint

from ..controllers.salas import Salas

salas_bp = Blueprint('salas_bp', __name__)

salas_bp('/', methods=['GET'])(Salas.get_all)
#salas_bp('/<int:<id_salas>', methods=['GET'])(Salas.get)
salas_bp('/', methods=['POST'])(Salas.create)
#salas_bp('/<id_salas>', methods=['PUT'])(Salas.update)
salas_bp('/<int:id_salas>', methods=['DELETE'])(Salas.delete)