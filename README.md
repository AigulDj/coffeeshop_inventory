# Coffee Shop Inventory Management Application

A web-based application to help coffee shop owners keep track of purchases, ingredients, menu items, and more. 
The app features the following functionalities:

- An inventory of ingredients, including available quantity and prices per unit
- A list of menu items and their prices
- Recipe requirements for each menu item
- A log of all purchases made at the coffee shop

With this information, coffee shop owners can:

- Add new menu items, including their recipe requirements and costs
- Add new ingredients to the inventory, including their prices and quantities
- Record customer purchases, which automatically updates the inventory and purchase log

To run the application using Docker, execute the following commands:

- docker pull aiguldj/coffeeshop-inventory:latest
- docker run --name coffeeshop -d -p 8000:8000 aiguldj/coffeeshop-inventory:latest

Note: The container name can be changed to your liking.

The application is built using Django, Python, SQLite, and a REST API. The user interface is designed with HTML5 and CSS3 (Bootstrap).
