from database import db
from models.order import Order
from sqlalchemy import select
from datetime import date
from models.cart import Cart

class OrderService:

    @staticmethod
    def save(order_data):

        cart_id = order_data.get('cart_id')
        

        cart = db.session.query(Cart).filter_by(id=cart_id).first()
        if not cart:
            raise ValueError("no find")
        

        new_order = Order(customer_id=cart.customer_id, date=date.today())
        db.session.add(new_order)
        db.session.commit()


        db.session.refresh(new_order)


        db.session.delete(cart)  


        db.session.commit()

        return new_order

    @staticmethod
    def find_all(page=1, per_page=10):
        query = select(Order)
   
        all_orders = db.paginate(query, page=int(page), per_page=int(per_page))
        return all_orders
