# About the Project

This is the third project I have done for CS50’s Web Programming with Python and Javascript class on edx.org.
The objectives of the project were:
* Become more comfortable with Django.
* Gain experience with relational database design.

For that purpose, I've built a web application for handling menu orders based on the Pinocchio's Pizza & Subs restaurant (http://www.pinocchiospizza.net/menu.html), where users can create accounts on the app to order items from the menu.

# Features

1. **Menu**: The menu is categorized into Regular Pizza, Sicilian Pizza, Sub, Pasta, Salad and Dinner Platter. When an item is clicked, additional information will appear if the user is logged in, in which the user can choose the size of the item and which toppings/addons they would like (if available). I interpreted Special Pizza as pizza with 4 toppings.
2. **Adding Items**: When a user has a staff (admin) status, he/she can access http://127.0.0.1:8000/admin to add, update or remove menu items on the menu database.
3. **Registration, Login, Logout**: Customers can create an account with their username, password, first name, last name and email address. Using this account, they can login and logout. Customers can only place orders when they are logged in.
4. **Shopping Cart**: When an item on the menu is clicked, a button called "Add to cart" appears if the user is logged in. When this button is clicked, an alert will appear confirming that the item has been added to the user's shopping cart. This cart can be accessed in the shopping cart page of the app.
5. **Placing an Order**: On the shopping cart page, users can only place an order (proceed to checkout) when there is at least one item in the cart. If there aren't any, the button "Proceed to checkout" will not appear. When the user clicks on "Proceed to checkout", he/she will be asked to confirm the items and the total price before placing the order.
6. **Viewing Orders**: Admins can look at a list of all orders that have ever been placed in the Orders page of the app. 
7. **Personal Touch: Changing Order Status (admin) and Tracking Order Progress (customer)**: In the Orders page, if the user is an admin, he/she can change the status of an order to "Completed". If the user is a customer, he/she will see a list of their pending and completed orders. An order is pending for a customer if its status hasn't been changed to "Completed" by the admin.

# Installation

1. Download this repository.
2. Install all the packages needed by executing: `pip3 install -r requirements.txt` on Terminal.
3. Run the application: `python3 manage.py runserver`
4. Go to the local address specified by typing it in your browser, most likely: http://127.0.0.1:8000/

# File Contents

1. /orders/static folder: contains .css, .js, .png, .jpg and font files
2. /orders/templates folder: contains index.html: the first page that is displayed when the user goes to http://127.0.0.1:8000/ on the browser; register.html: the registration page; login.html: the login page; orders_list.html: the page with a list of orders; shopping_cart.html: the page with items in the shopping cart
3. /orders/migrations folder: contains all migrations that have ever been made to the database
4. /orders/urls.py: contains information about the paths of the web app and associates them each to a view
5. /orders/views.py: associates a view with an HTML page, and transfers information for the HTML page to display
6. /orders/models.py: contains the structure of each table in the database
7. /orders/admin.py: registers database models to the admin site, so they can be viewed, updated or deleted
8. /pizza/settings.py: added STATIC_URL, which is configured to the /static folder of each app
