from database import db, Base

# order_product = db.Table(
#     'Order_Product',
#     Base.metadata,
#     db.Column('order_id', db.ForeignKey('orders.id')),
#     db.Column('product_id', db.ForeignKey('products.id'))
# )

class OrderProduct(db.Model):
    __tablename__ = 'order_product'
    
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)

    unit_price = db.Column(db.Float, nullable=False)
