from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services.orderService import OrderService
from marshmallow import ValidationError
from utils.util import token_required


@token_required
def save():
    try:
    
        cart_id = request.json.get('cart_id')

        if not cart_id:
            raise ValueError("Cart ID is required.")


        new_order = OrderService.save({"cart_id": cart_id})


        return jsonify({"message": "订单创建成功", "order_id": new_order.id}), 201
    except ValueError as e:

        return jsonify({"error": str(e)}), 400
    except ValidationError as e:

        return jsonify(e.messages), 400

@token_required
def find_all():

    page = request.args.get("page", 1)
    per_page = request.args.get("per_page", 10)

    try:

        all_orders = OrderService.find_all(page, per_page)
        return orders_schema.jsonify(all_orders), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
