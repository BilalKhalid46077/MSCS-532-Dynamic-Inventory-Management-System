# Project: Dynamic Inventory Management System Using Python
# Phase 3 - Optimization, Scaling, and Final Evaluation
# Bilal Khalid
# Algorithms and Data Structures

# This program is an optimized version of the Phase 2 inventory management system.

# Optimizations:
# 1. Better code organization
# 2. Faster category searching
# 3. Product statistics
# 4. Performance timing
# 5. Better error handling
# 6. Modular functions

from collections import deque
import time

# Product Class

class Product:
    # Represents a single product.

    def __init__(self, product_id, name, quantity, price, category):

        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

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

        # Main Inventory
        self.inventory = {}

        # Queue for low stock products
        self.restock_queue = deque()

        # NEW:
        # Stores products category-wise
        # Makes category search faster
        self.category_index = {}

        self.minimum_stock = 10


    # ---------------------------------------------------

    def add_product(self, product):

        if product.product_id in self.inventory:

            print("Product already exists.\n")
            return

        # Store inside dictionary
        self.inventory[product.product_id] = product

        # Store inside category dictionary

        if product.category not in self.category_index:

            self.category_index[product.category] = []

        self.category_index[product.category].append(product)

        print("Product added successfully.")


    # ---------------------------------------------------

    def search_product(self, product_id):

        return self.inventory.get(product_id)


    # ---------------------------------------------------

    def update_quantity(self, product_id, quantity):

        product = self.search_product(product_id)

        if product is None:

            print("Product not found.\n")
            return

        product.quantity = quantity

        if quantity < self.minimum_stock:

            self.add_restock(product_id)


    # ---------------------------------------------------

    def update_price(self, product_id, price):

        product = self.search_product(product_id)

        if product:

            product.price = price

        else:

            print("Product not found.\n")


    # ---------------------------------------------------

    def delete_product(self, product_id):

        product = self.search_product(product_id)

        if product is None:

            print("Product not found.\n")
            return

        self.category_index[product.category].remove(product)

        del self.inventory[product_id]

        print("Product deleted.")


    # ---------------------------------------------------

    def display_inventory(self):

        print("\n------ INVENTORY ------")

        if len(self.inventory) == 0:

            print("Inventory Empty\n")
            return

        for product in self.inventory.values():

            print(product.product_id,
                  product.to_dictionary())

        print()


    # ---------------------------------------------------

    def display_category(self, category):

        print(f"\nCategory : {category}")

        products = self.category_index.get(category)

        if products is None:

            print("No products found.\n")
            return

        for product in products:

            print(product.product_id,
                  product.to_dictionary())

        print()


    # ---------------------------------------------------

    def add_restock(self, product_id):

        if product_id not in self.restock_queue:

            self.restock_queue.append(product_id)


    # ---------------------------------------------------

    def process_restock(self):

        if len(self.restock_queue) == 0:

            print("No products to restock.\n")
            return

        product = self.restock_queue.popleft()

        print("Restocking:", product)


    # ---------------------------------------------------

    def total_products(self):

        return len(self.inventory)


    # ---------------------------------------------------

    def total_inventory_value(self):

        # Optimization:
        # Calculate total inventory value.

        total = 0

        for product in self.inventory.values():

            total += product.price * product.quantity

        return total


    # ---------------------------------------------------

    def performance_test(self, product_id):

        # Measures search time.

        start = time.perf_counter()

        self.search_product(product_id)

        end = time.perf_counter()

        return end - start
