from . import ma
from marshmallow import fields,Schema

#incoming cart data
'''
{
    "customer_id": int,
    "product_ids": [ints] list of product ids that will be used to create the relationship from this cart to all the products
}
'''

class cartSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=False) #will generate the date for each cart inside the service
    customer_id = fields.Integer(required=True)
    products = fields.Nested("ProductSchema", many=True)

    class Meta:
        fields = ('id', 'date', 'customer_id', 'product_ids','products') #need product_ids in  fields so they can be passed in

cart_schema = cartSchema()
carts_schema = cartSchema(many=True)

