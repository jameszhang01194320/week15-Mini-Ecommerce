#cartController.py
from flask import request, jsonify
from models.schemas.cartSchema import cart_schema, carts_schema
from services import cartService
from marshmallow import ValidationError
from utils.util import token_required

def save():
    try:
        cart_data = cart_schema.load(request.json)
        new_cart = cartService.save(cart_data)
        return cart_schema.jsonify(new_cart), 201
    except ValidationError as e:
        return jsonify(e.messages), 400

@token_required
def find_all():
    page = request.args.get("page")
    per_page = request.args.get("per_page")
    page = 1 if not page else page
    per_page = 10 if not per_page else per_page
    all_carts = cartService.find_all_carts(page, per_page)
    
    return carts_schema.jsonify(all_carts), 200

def find_by_id(cart_id): #dynamic route takes in parameters
    order = cartService.find_by_id(cart_id)

    return cart_schema.jsonify(order), 200

# update
def update(cart_id):
    try:
        cart_data = cart_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_cart = cartService.update_cart(cart_id, cart_data)
    if not updated_cart:
        return jsonify({"message": "Cart not found"}), 404

    return cart_schema.jsonify(updated_cart), 200


# delete
def delete(cart_id):
    deleted_cart = cartService.delete_cart(cart_id)
    if not deleted_cart:
        return jsonify({"message": "Cart not found"}), 404

    return jsonify({"message": f"Cart with ID {cart_id} deleted successfully."}), 200

