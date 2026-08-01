# Performance Testing

# This file creates a large inventory to test scalability.

import random

from optimized_inventory_system import Inventory
from optimized_inventory_system import Product


inventory = Inventory()

# Generate Large Dataset

print("Creating Products...\n")

for i in range(1, 10001):

    product = Product(

        f"P{i}",

        f"Product{i}",

        random.randint(5, 200),

        random.randint(100, 1000),

        random.choice([
            "Food",
            "Electronics",
            "Stationery",
            "Clothing"
        ])

    )

    inventory.add_product(product)


print()

print("Products Created Successfully.")

print()

print("Total Products :",
      inventory.total_products())

print()

# Search Performance

search_time = inventory.performance_test("P9999")

print("Search Time:")

print(search_time)

print()

# Inventory Value

print("Inventory Value:")

print(inventory.total_inventory_value())

print()

# Category Search

inventory.display_category("Food")

# Low Stock Test

inventory.update_quantity("P500", 3)

inventory.process_restock()
