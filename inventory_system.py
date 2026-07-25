# Project: Dynamic Inventory Management System Using Python
# Phase 2 - Proof of Concept
# Bilal Khalid
# Algorithms and Data Structures

# Queue implementation
from collections import deque

# Product Class
class Product:
    # This class represents a single product.
    
    def __init__(self, product_id, name, quantity, price, category):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    # Convert object into dictionary format
    def to_dictionary(self):
        return {
            "Name": self.name,
            "Quantity": self.quantity,
            "Price": self.price,
            "Category": self.category
        }

# Inventory Class
class Inventory:

    def __init__(self):

        # Dictionary (Hash Table)
        # Product ID is the key
        self.inventory = {}

        # Queue used for restocking requests
        self.restock_queue = deque()

        # Minimum quantity before restocking
        self.minimum_stock = 10

    def add_product(self, product):
        # Add a new product to inventory.

        if product.product_id in self.inventory:
            print("Product already exists.\n")
            return

        self.inventory[product.product_id] = product

        print("Product added successfully.\n")

    def search_product(self, product_id):
        # Search product using Product ID.

        if product_id in self.inventory:

            print("Product Found")

            print(self.inventory[product_id].to_dictionary())

            return self.inventory[product_id]

        print("Product not found.\n")

        return None

    def update_quantity(self, product_id, new_quantity):

        # Update product quantity.
        if product_id not in self.inventory:
            print("Product does not exist.\n")
            return

        self.inventory[product_id].quantity = new_quantity

        print("Quantity updated successfully.\n")

        # Add to restock queue if quantity becomes low
        if new_quantity < self.minimum_stock:

            self.add_restock_request(product_id)

    def update_price(self, product_id, new_price):
        # Update product price.

        if product_id not in self.inventory:
            print("Product does not exist.\n")
            return

        self.inventory[product_id].price = new_price

        print("Price updated successfully.\n")

    def delete_product(self, product_id):
        # Delete a product.

        if product_id not in self.inventory:

            print("Product not found.\n")

            return

        del self.inventory[product_id]

        print("Product deleted successfully.\n")

    def display_inventory(self):
        # Display every product.
        # Dictionary values are converted into a list.

        print("\n------ COMPLETE INVENTORY ------")

        product_list = list(self.inventory.values())

        if len(product_list) == 0:

            print("Inventory is empty.\n")

            return

        for product in product_list:

            print(product.product_id, product.to_dictionary())

        print()

    def display_category(self, category):
        
        # Display products of one category.
        print(f"\nProducts in Category : {category}")

        found = False

        for product in self.inventory.values():

            if product.category.lower() == category.lower():

                print(product.product_id, product.to_dictionary())

                found = True

        if not found:

            print("No products found.")

        print()

    def add_restock_request(self, product_id):

        # Add product into queue.
        if product_id not in self.restock_queue:

            self.restock_queue.append(product_id)

            print("Restock request added.\n")

    def process_restock(self):

        # Process first request in queue.
        if len(self.restock_queue) == 0:

            print("No restocking requests.\n")

            return

        product = self.restock_queue.popleft()

        print(f"Restocking Product : {product}\n")

    def inventory_size(self):
        
        # Display total products.
        print("Total Products :", len(self.inventory))
