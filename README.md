# MSCS-532-Dynamic-Inventory-Management-System

## Project Overview

This project is a **Proof of Concept (PoC)** developed for Phase 2 of the course project **"Developing and Optimizing Data Structures for Real-World Applications Using Python."** The objective is to demonstrate how different data structures can be used to solve a real-world inventory management problem.

The application simulates a simple inventory management system that allows users to store products, search for products, update inventory information, delete products, display products, and manage low-stock restocking requests. The project focuses on implementing the core functionality rather than developing a complete commercial application.

---

## Project Objectives

The main objectives of this project are:

- Demonstrate the practical use of data structures in Python.
- Implement the core operations of an inventory management system.
- Follow modular programming and object-oriented programming principles.
- Produce readable, well-documented, and maintainable code.
- Create a proof of concept that can be expanded in future project phases.

---

## Data Structures Used

### 1. Dictionary (Hash Table)

A Python dictionary is used as the primary data structure for storing inventory records. Each product is stored using its unique Product ID as the key, allowing fast searching, updating, and deletion.

Example operations:
- Add Product
- Search Product
- Update Product
- Delete Product

Average Time Complexity:
- Insert: O(1)
- Search: O(1)
- Delete: O(1)

---

### 2. List

A Python list is used to display all products and to filter products by category. It is mainly used for traversal and reporting purposes.

Example operations:
- Display Inventory
- Display Products by Category

Average Time Complexity:
- Traversal: O(n)

---

### 3. Queue

The project uses Python's `collections.deque` to implement a queue for managing restocking requests.

Products with low stock are automatically added to the restocking queue and processed using the First-In, First-Out (FIFO) principle.

Example operations:
- Add Restock Request
- Process Restock Request

Average Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)

---

## Project Features

The proof of concept currently supports the following features:

- Add new products
- Search products using Product ID
- Update product quantity
- Update product price
- Delete products
- Display all inventory
- Display products by category
- Automatic restocking queue
- Process restocking requests
- Basic error handling
- Modular and reusable code

---

## Requirements

- Python 3.10 or later
- No external libraries are required.

Only one built-in Python module is used:

```
collections
```

---

## How to Run the Project

### Step 1

Download or clone the repository.

```
git clone 
```
---

### Step 2

Open the project folder.

---

### Step 3

Run the test file.

```
python test_inventory.py
```

---

## Sample Operations

The demonstration includes the following operations:

- Adding products
- Searching products
- Updating product quantity
- Updating product price
- Deleting products
- Viewing inventory
- Displaying products by category
- Processing restocking requests

---

## Example Output

```
Product added successfully.

Product Found

Quantity updated successfully.

Restock request added.

Price updated successfully.

Product deleted successfully.

Restocking Product : P103

Total Products : 2
```

---

## Testing

The proof of concept was tested using several scenarios, including:

- Adding multiple products
- Searching existing products
- Searching non-existing products
- Updating product quantity
- Updating product price
- Deleting products
- Displaying inventory
- Displaying products by category
- Automatic restocking queue generation
- Processing queue requests

The results confirmed that all implemented operations behaved as expected.

---

## Error Handling

The program includes simple error handling for common situations, such as:

- Duplicate Product IDs
- Product not found
- Empty inventory
- Empty restocking queue

These checks improve the reliability of the application.

---

## Future Improvements

This proof of concept can be extended by adding several advanced features, including:

- Graphical User Interface (GUI)
- Database integration (MySQL or PostgreSQL)
- Barcode scanner support
- Inventory reports
- User authentication
- Sales management
- Supplier management
- File storage
- Product expiration tracking
- Data visualization dashboard

---

## GitHub Repository

GitHub Repository:



---

## Author

**Student Name:** Bilal Khalid

**Course:** Algorithms and Data Structures (MSCS-532-B01)

**Project:** Developing and Optimizing Data Structures for Real-World Applications Using Python

**Phase:** Deliverable 2 – Proof of Concept

---

## License

This project was developed for educational purposes as part of a university assignment.
