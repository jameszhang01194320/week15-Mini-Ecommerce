# cartService.py
from database import db
from models.cart import Cart
from models.product import Product
from sqlalchemy import select
from datetime import date #need to get todays date for the cart
from models.cartProduct import cart_product


def save(cart_data):

    new_cart = Cart(customer_id=cart_data['customer_id'], date=date.today()) #date.today() will generate todays date and store it in the date catagory

    for item_id in cart_data['product_ids']:
        query = select(Product).where(Product.id==item_id) #search the product table for a product whose id is the same as the item_id we are looping over
        item = db.session.execute(query).scalar()
        new_cart.products.append(item) #creates the connection from Cart to the associate id, and populates our cart_product table

    db.session.add(new_cart)
    db.session.commit()

    db.session.refresh(new_cart)
    return new_cart

def find_all_carts(page=1, per_page=10):
    query = select(Cart)
    all_carts = db.paginate(query, page=int(page), per_page=int(per_page))
    return all_carts

def find_by_id(cart_id):
    query = select(Cart).where(Cart.id == cart_id)
    order = db.session.execute(query).scalar()
    return order





# Function to update an existing cart
def update_cart(cart_id, cart_data):
    cart = db.session.get(Cart, cart_id)
    if not cart:
        return None

    # Update cart details (e.g., date, products)
    cart.date = cart_data.get('date', cart.date)

    # Update products if provided
    if 'product_ids' in cart_data:
        cart.products.clear()  # Clear existing products
        products = db.session.execute(select(Product).filter(Product.id.in_(cart_data['product_ids']))).scalars().all()
        cart.products.extend(products)

    db.session.commit()
    db.session.refresh(cart)
    return cart






# Function to delete an cart by its ID
def delete_cart(cart_id):
    cart = db.session.get(Cart, cart_id)
    if not cart:
        return None

    db.session.delete(cart)
    db.session.commit()
    return cart


