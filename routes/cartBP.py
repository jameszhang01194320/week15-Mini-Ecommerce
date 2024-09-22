#cartBP.py
from flask import Blueprint

from controllers.cartController import save, find_all, find_by_id, update, delete


cart_blueprint = Blueprint("cart_bp", __name__)

cart_blueprint.route('/', methods=["POST"])(save)
cart_blueprint.route('/', methods=["GET"])(find_all)

cart_blueprint.route('/<int:cart_id>', methods=['GET'])(find_by_id)
cart_blueprint.route('/<int:cart_id>', methods=['PUT'])(update)
cart_blueprint.route('/<int:cart_id>', methods=['DELETE'])(delete)