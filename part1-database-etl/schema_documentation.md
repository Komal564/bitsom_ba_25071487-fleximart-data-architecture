=======================================================
 ## FLEXIMART DATABASE SCHEMA DOCUMENTATION
=======================================================

-------------------------------------------------------
  ## 1. SYSTEM OVERVIEW
------------------------------------------------------------

This document explains the complete relational database schema
implemented for the Fleximart e-commerce ETL pipeline. The schema
stores structured and validated data after successful execution
of extract, transform, and load processes.

The database is designed with a strong focus on:
- Data accuracy and consistency
- Clear separation of business entities
- Efficient transactional processing
- Reliable analytical querying
- Strict adherence to normalization rules

--------------------------------------------------------
## 2. DATABASE INFORMATION
--------------------------------------------------------

Database Name   : FLEXIMART
  
All data is ingested into the database through a Python-based ETL
pipeline after passing quality checks and transformations.

--------------------------------------------------------
## 3. INPUT DATA SOURCES
--------------------------------------------------------

The ETL pipeline processes the following raw CSV files:

- customers_raw(1).csv
- products_raw.csv
- sales_raw.csv

Each dataset is cleaned, standardized, validated, and then loaded
into the corresponding relational tables.

-------------------------------------------------------
## 4. ENTITY DEFINITIONS
-------------------------------------------------------

=======================================================
## ENTITY : CUSTOMERS
=======================================================

## Description  
The customers entity stores master-level information for every
customer registered on the Fleximart platform. This table acts
as the base reference for all customer-related transactions.

## Attributes  
- customer_id        : System-generated unique customer identifier  
- first_name         : Customer’s given name  
- last_name          : Customer’s family name  
- email              : Unique customer email address  
- phone              : Standardized phone number (+91XXXXXXXXXX)  
- city               : City of residence  
- registration_date  : Date of customer registration  

## Relationships  
- One customer can place multiple orders  

## Source  
- customers_raw(1).csv (after ETL processing)

## Constraints  
- customer_id is the Primary Key  
- email must be unique  
- Invalid or incomplete records are excluded during ETL  

-------------------------------------------------------
=======================================================
## ENTITY : PRODUCTS
=======================================================

## Description  
The products entity stores all product catalog information
available for sale on the Fleximart platform.

## Attributes  
- product_id        : System-generated unique product identifier  
- product_name      : Name of the product  
- category          : Product classification(Electronics,Fashion,Groceris,other)  
- price             : Selling price  
- stock_quantity    : Available inventory quantity  

## Relationships  
- One product can appear in multiple order items  

## Source  
- products_raw.csv (after ETL processing)

## Constraints  
- product_id is the Primary Key  
- Missing prices are imputed using category median  
- Missing stock values are replaced with zero  

--------------------------------------------------------
=======================================================
## ENTITY : ORDERS
=======================================================

## Description  
The orders entity captures order-level transactional data for
each purchase made by a customer.

## Attributes  
- order_id       : System-generated unique order identifier  
- customer_id    : Identifier of the customer placing the order  
- order_date     : Date of transaction  
- total_amount   : Total monetary value of the order  

## Relationships  
- Each order belongs to one customer  
- Each order can contain multiple order items  

## Source  
- sales_raw.csv (after ETL processing)

## Constraints  
- order_id is the Primary Key  
- customer_id is a Foreign Key referencing Customers  
- Orders are inserted only when a valid customer exists  

------------------------------------------------------------

=======================================================
## ENTITY : ORDER_ITEMS
=======================================================

## Description  
The order_items entity stores item-level details for each order,
capturing the products purchased and their quantities.

## Attributes  
- order_item_id  : System-generated unique order item identifier  
- order_id       : Identifier of the associated order  
- product_id     : Identifier of the purchased product  
- quantity       : Number of units purchased  
- unit_price     : Product price at purchase time  
- subtotal       : Calculated as quantity × unit_price  

## Relationships  
- Multiple order items belong to one order  
- Each order item references one product  

## Source  
- Derived from sales_raw.csv during ETL processing  

## Constraints  
- order_item_id is the Primary Key  
- order_id is a Foreign Key referencing Orders  
- product_id is a Foreign Key referencing Products  
- Records inserted only after successful validation  

-------------------------------------------------------
## 5. RELATIONSHIP SUMMARY
-------------------------------------------------------

- Customers → Orders       : One-to-Many  
- Orders → Order_Items     : One-to-Many  
- Products → Order_Items   : One-to-Many  

This structure ensures clean data flow and strict referential
integrity across the database.

----------------------------------------------------

## 6 NORMALIZATION EXPLANATION (3NF)

The FlexiMart database schema is designed following Third Normal Form (3NF)
principles to ensure data integrity and minimize redundancy.

In this design, each table represents a single entity, and all non-key
attributes depend only on the primary key of their respective table.
There are no partial dependencies or transitive dependencies present.

Customer-related attributes such as name, email, and city are stored only
in the customers table. Product-related details like product name, category,
price, and stock are stored only in the products table. Transactional data
is split between orders and order_items to avoid repeating order-level
information for each product purchased.

This design avoids:
- **Update anomalies:** Customer or product information can be updated in
  one place without affecting multiple records.
- **Insert anomalies:** New customers or products can be inserted without
  requiring an order.
- **Delete anomalies:** Deleting an order does not remove customer or product
  data.

Thus, the schema fully satisfies Third Normal Form requirements and is well
suited for transactional processing and analytical reporting.

-------------------------------------------------------

----------------------------
## 7. Functional Dependencies
----------------------------

* Customers  
customer_id → first_name, last_name, email, phone, city, registration_date  

* Products  
product_id → product_name, category, price, stock_quantity  

* Orders  
order_id → customer_id, order_date, total_amount  

* Order_Items  
order_item_id → order_id, product_id, quantity, unit_price, subtotal  

This confirms that the schema strictly satisfies Third Normal Form.


--------------------------------------------------------
## 8. FINAL CONCLUSION
--------------------------------------------------------

The Fleximart relational database schema provides a robust,
normalized, and scalable foundation for the ETL pipeline.
The design ensures strong data integrity, efficient querying,
and long-term maintainability for analytical and transactional
use cases.

--------------------------------------
## 9. SAMPLE DATA REPRESENTATION
----------------------------------------

### customers

| customer_id | first_name | last_name | email              | city   |
|------------|-----------|-----------|--------------------|--------|
| 1          | Rahul     | Sharma    | rahul@gmail.com    | Delhi  |
| 2          | Anjali    | Verma     | anjali@gmail.com   | Mumbai |

---

### products

| product_id | product_name        | category     | price  |
|-----------|---------------------|-------------|--------|
| 1         | Samsung Galaxy S21  | Electronics | 45999  |
| 2         | Nike Running Shoes | Fashion     | 3499   |

---

### orders

| order_id | customer_id | order_date | total_amount |
|---------|------------|------------|--------------|
| 101     | 1          | 2024-01-15 | 49998        |
| 102     | 2          | 2024-01-18 | 3499         |

---

### order_items

| order_item_id | order_id | product_id | quantity | subtotal |
|--------------|----------|------------|----------|----------|
| 1            | 101      | 1          | 1        | 45999    |
| 2            | 102      | 2          | 1        | 3499     |


