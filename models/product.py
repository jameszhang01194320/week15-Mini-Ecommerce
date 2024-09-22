# product.py
from database import db
from models.cartProduct import cart_product  #

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

 
    carts = db.relationship('Cart', secondary=cart_product, back_populates='products')
