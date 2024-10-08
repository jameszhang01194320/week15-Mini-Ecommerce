from . import ma
from marshmallow import fields

class CustomerSchema(ma.Schema): #Inherting our instance of Marshmallow 
    id = fields.Integer(required=False) #This will be auto-incremented
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True) 
    username = fields.String(required=True)
    password = fields.String(required=True)
  
    class Meta:
        fields = ("id", "name", "email", "phone", "username", "password")

customer_schema = CustomerSchema() #instantiate a single customer schema
customers_schema = CustomerSchema(many=True, exclude=["password"])
customer_login = CustomerSchema(exclude=["name", 'phone', 'username', 'id'])