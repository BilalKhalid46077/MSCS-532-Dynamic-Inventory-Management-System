# Dynamic Inventory Management System Using Python (Phase 3)

## Project Overview

This project was developed for **Phase 3** of the course project **"Developing and Optimizing Data Structures for Real-World Applications Using Python."** The purpose of this phase is to optimize the proof of concept developed in Phase 2 by improving performance, scalability, and testing.

The project demonstrates how efficient data structures can be used to manage inventory operations in a business environment. The optimized implementation supports product management, category indexing, restocking requests, and performance testing with large datasets.

---

# Project Objectives

The main objectives of this phase are:

- Optimize the data structures developed in Phase 2.
- Improve search and category lookup performance.
- Test the system with a large number of products.
- Analyze scalability and execution time.
- Follow Python programming best practices.

---

# Data Structures Used

## 1. Dictionary (Hash Table)

The inventory is stored in a Python dictionary where each Product ID is the key.

Example operations:

- Add Product
- Search Product
- Update Product
- Delete Product

Average Time Complexity:

| Operation | Complexity |
|----------|------------|
| Insert | O(1) |
| Search | O(1) |
| Update | O(1) |
| Delete | O(1) |

---

## 2. Category Index (Optimized Dictionary)

A second dictionary stores products according to their category.

Instead of searching through every product, the system directly retrieves products from the selected category.

Example:

```
Food
    Rice
    Sugar
    Bread

Electronics
    Laptop
    Keyboard
```

This optimization reduces unnecessary traversal when displaying products by category.

---

## 3. Queue (Deque)

Python's `collections.deque` is used to maintain restocking requests.

Whenever product quantity falls below the minimum stock level, the Product ID is automatically added to the queue.

The queue follows the FIFO (First In First Out) principle.

Average Time Complexity:

| Operation | Complexity |
|----------|------------|
| Enqueue | O(1) |
| Dequeue | O(1) |

---

# Optimizations Implemented

Compared to Phase 2, several improvements were introduced.

- Added a category index for faster category searching.
- Improved error handling.
- Added inventory statistics.
- Added search performance timing.
- Added support for testing large datasets.
- Improved modular programming.
- Improved code readability and maintainability.

---


# Requirements

- Python 3.10 or newer

Built-in modules used:

```
collections
time
random
```

No external libraries are required.

---

# How to Run

## Step 1

Clone the repository.

```
git clone https://github.com/BilalKhalid46077/MSCS-532-Dynamic-Inventory-Management-System.git
```
---

## Step 2

Open the project folder.

---

## Step 3

Run the performance testing script.

```
py performance_test.py
```

---

# Features

The optimized system supports:

- Add Product
- Search Product
- Update Quantity
- Update Price
- Delete Product
- Display Inventory
- Display Products by Category
- Restocking Queue
- Performance Measurement
- Large Dataset Testing
- Inventory Statistics
- Error Handling

---

# Performance Testing

The project generates approximately **10,000 products** to evaluate scalability.

The following tests are performed:

- Product insertion
- Product searching
- Category lookup
- Inventory statistics
- Restocking queue
- Execution time measurement

---

# Output

<img width="608" height="642" alt="image" src="https://github.com/user-attachments/assets/ec2b76cf-1920-47d1-9763-034cb6fa0ca7" />


---

# Performance Improvements

| Phase 2                 | Phase 3                    |
|-------------------------|----------------------------|
| Basic inventory         | Optimized inventory        |
| Dictionary only         | Dictionary + Category Index|
| Small dataset           | 10,000 products            |
| Manual testing          | Automated testing          |
| No performance analysis | Search timing              |           
| Basic validation        | Improved validation        |

---

# Testing

The following tests were completed successfully.

- Add product
- Delete product
- Search product
- Update quantity
- Update price
- Display inventory
- Category search
- Restocking queue
- Large dataset testing
- Performance timing

---

# Future Improvements

Future versions of this project can include:

- MySQL database integration
- Graphical User Interface (GUI)
- Barcode scanner support
- Product sales management
- Supplier management
- Inventory reports
- Login system
- Cloud database integration
- Data visualization dashboard
- REST API support

---

# Author

Student Name: Bilal Khalid

Course: Algorithms and Data Structures (MSCS-532-B01)

Project: Developing and Optimizing Data Structures for Real-World Applications Using Python

Deliverable: Phase 3 – Optimization, Scaling, and Final Evaluation

---
