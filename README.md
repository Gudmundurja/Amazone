# Amazone E-Commerce Database (MongoDB)
Amazone is a fictional e-commerce backend system. This project demonstrates a complete NoSQL database implementation using MongoDB, with extensive focus on schema design, synthetic data generation, advanced querying, and distributed system design for scalability.

# Key Components
# Backend Implementation
MongoDB database design following NoSQL principles.

Collections include: Products, Customers, Carts, Orders, Stores, Warehouses, Partners, Product_Ratings, Partner_Ratings, and more.

Uses document referencing and embedding with patterns like bucket and polymorphic where appropriate.

# Synthetic Data Generation
Python scripts to generate realistic and structured JSON data.

Data simulates real-world orders, ratings, partners, and product catalogues.

Ensures consistency across collections with shared Customer_ID, Product_ID, Order_ID, etc.

# Intelligent Queries
Recommended_products.py:

Calculates and stores each customer's top 2 highest-rated products using ratings from Product_rating collection.

Efficient querying using MongoDB indexing on Customer_ID.

Final recommendations are embedded into each customer document.

python
Copy
Edit
"Recommended_Products": [
    {"Product_ID": 34, "Name": "Treeflex", "Average_customer_rating": 5, "Price": 10.99},
    {"Product_ID": 40, "Name": "Y-find", "Average_customer_rating": 5, "Price": 16.99}
]
# Maintenance Queries
Queries to remove expired carts and automatically restock inventory in:

Carts

Other_Product_Warehouse_Storage

Stores

Daily_Inventory_Level


# theoretical question - how would it be implmented if we were to start Scaling to the EU?

# Replication Strategy
Multi-Leader Replication recommended for geo-distribution and high availability.

Resolves conflicts using synchronous conflict detection between data centres.

# Partitioning
Implements Hash Partitioning to balance load across nodes (instead of Key-Range).

Proposes redesign of IDs and addresses for easier EU expansion and querying.

# Example Files Included
Products.json – full product catalogue with nested structures.

Partner_rating.json, Partners.json, Store.json, Warehouse.json, Past_order_ISO_json.txt, Product_rating_Json.txt.

Recommended_products.py – logic for top-rated recommendations.

README.md – this file.

# Learning Outcomes
Mastered MongoDB schema design with large synthetic datasets.

Learned the trade-offs of referencing vs. embedding in NoSQL.

Gained practical experience in replication, partitioning, and scaling strategies.

Significantly improved Python + MongoDB scripting skills for data engineering.
