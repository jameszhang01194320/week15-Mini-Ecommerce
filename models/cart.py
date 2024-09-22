# cart.py
from database import db
from models.cartProduct import cart_product  # 

class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    date = db.Column(db.Date, nullable=False)


    products = db.relationship('Product', secondary=cart_product, back_populates='carts')


    customer = db.relationship('Customer', back_populates='carts')
