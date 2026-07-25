# Simple testing script

# This demonstrates the major operations of the inventory management system.

from inventory_system import Product
from inventory_system import Inventory


# Create inventory object
store = Inventory()

# Add Products

product1 = Product(
    "P101",
    "Rice",
    100,
    350,
    "Food"
)

product2 = Product(
    "P102",
    "Milk",
    50,
    180,
    "Dairy"
)

product3 = Product(
    "P103",
    "Soap",
    8,
    120,
    "Personal Care"
)


store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

# Display Inventory
store.display_inventory()

# Search Product
store.search_product("P102")

# Update Quantity
store.update_quantity("P103", 5)

# Update Price
store.update_price("P102", 200)

# Display Category
store.display_category("Food")

# Delete Product
store.delete_product("P101")

# Display Inventory Again
store.display_inventory()

# Process Restocking Queue
store.process_restock()

# Total Products
store.inventory_size()