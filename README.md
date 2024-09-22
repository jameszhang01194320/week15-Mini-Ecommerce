Mini-Project: Advanced E-commerce API
Project Requirements

1.	Customer: Create the following endpoints for managing Customers and their associates:
Create Customer: Implement an endpoint to add a new customer to the database. Ensure that you capture essential customer information, including name, email, and phone number.
Read Customers: Develop an endpoint to retrieve all customer details. Provide functionality to query and display customer information.
Login: Takes the user's credentials and returns a token

2.	Products: Create the following endpoints for managing Products:
Create Product: Implement an endpoint to add a new product to the e-commerce database. Capture essential product details, such as the product name and price.
List Products: Develop an endpoint to list all available products in the e-commerce platform. Ensure that the list provides essential product information.

3.	Order Processing: Develop comprehensive Orders Management functionality to efficiently handle customer orders, ensuring that customers can place, and track their orders seamlessly.
Place Order: Create an endpoint for customers to place new orders, orders should be generated from the products in the Customer's cart, and will no longer depend on passing product id's through the POST request.
Retrieve Order: Implement an endpoint that allows customers to retrieve details of a specific order based on user's identifier (ID). Provide a clear overview of the order, including the order date and associated products.

4.	Shopping cart: The Shopping Cart functionality is a crucial component of any e-commerce platform, allowing customers to add, and remove items they wish to purchase. Here's how you can develop a comprehensive Shopping Cart feature: 
Add Items to Cart: Create an endpoint that allows customers to add items to their shopping cart. Customers should be able to specify the quantity of each item they want to add. (DO NOT FORGET TO ADD AND COMMIT THE CUSTOMER AFTER ADDING ITEMS)
Remove Items from Cart: Implement functionality that enables customers to remove items from their shopping cart.
View Cart: Create an endpoint that allows customers to view their shopping cart, displaying a list of items. Ensure that the cart's content is displayed clearly and that customers can easily navigate the cart.
Empty Cart: Implement functionality that allows customers to clear their shopping cart, removing all items.
Place Order: Use the items in the cart to create and order, and empty the user's cart.

5.	Database Integration:
Utilize Flask-SQLAlchemy to integrate a MySQL database into the application.
Design and create the necessary Model to represent customers, orders, products, order_products, and cart (cart should be an association table between Customer and Product reference order_product
Establish relationships between tables to model the application's core functionality.
Ensure proper database connections and interactions for data storage and retrieval.

6.	Modularization code:
The code must be modularized using a layered architecture. The organization of the project must be composed as follows: Controllers, Models, Routes, Services, Utils
The code must have a configuration file to configure all database connections, cache, etc.

7.	Performance improvement with cache and limit implementation (WHERE YOU SEE NECESSARY):
Use the cache logic only to get requests using the flask-caching library.
Use flask-limiter to limit request consumption to 100 per day for all endpoints generated.

8.	Implement JWT Security 9. Document API with Swagger library:
Utilize JWT to add Token auth to your project and protect necessary routes ex. Routes

9.	Document API with Swagger library:
Use the Swagger library to be able to generate project documentation
Generate the swagger.yaml file with the documentation of each of the generated endpoints.
The Swagger documentation must have the security implementation by jwt.
10.	GitHub Repository:
Create a GitHub repository for the project and commit code regularly.
Maintain a clean and interactive README.md file in the GitHub repository, providing clear instructions on how to run the application and explanations of its features.
Include a link to the GitHub repository in the project documentation.

11.	Project
├── Customer
│   ├── Create Customer
│   ├── Read Customers
│   ├── Login
│   └── Associates (if any specific endpoints for associates)
├── Products
│   ├── Create Product
│   └── List Products
├── Order Processing
│   ├── Place Order
│   └── Retrieve Order
└── Shopping Cart
├── Add Items to Cart
├── Remove Items from Cart
├── View Cart
├── Empty Cart


