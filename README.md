# coffeeshop_inventory
Application that will help keep track of purchases, ingredients, menu items etc.

The owner of the coffee shop will be able to look through:
- An inventory of different Ingredients, their available quantity, and their prices per unit
- A list of the MenuItems, and the price set for each entry
- A list of the ingredients that each menu item requires (RecipeRequirements)
- A log of all Purchases made at the restaurant

Knowing that information, The user will be able to use the following features:
- Enter in new recipes along with their recipe requirements, and how much that menu item costs.
- Add to the inventory a name of an ingredient, its price per unit, and how much of that item is available.
- Enter in a customer purchase of a menu item. When a customer purchases an item off the menu, 
the inventory will be modified to accommodate what happened, as well as recording the time that the purchase was made.

#### Docker commands to pull the image from docker hub & run the container:

- docker pull aiguldj/coffeeshop-inventory:latest
- docker run --name coffeeshop -d -p 8000:8000 aiguldj/coffeeshop-inventory:latest
