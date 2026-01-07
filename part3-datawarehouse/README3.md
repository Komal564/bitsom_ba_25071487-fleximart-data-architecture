# Part 3: Data Warehouse & Analytics – FlexiMart

## Overview

This part of the FlexiMart Data Architecture project focuses on designing and implementing a **Data Warehouse** to analyze historical sales data. A **Star Schema** is used to support analytical processing (OLAP), enabling efficient aggregation, drill-down, roll-up, and customer segmentation analysis.

Part 3 includes:
- Star schema design documentation
- Data warehouse schema implementation
- Loading of analytical (dummy) data
- OLAP and business analytics queries

---

## Project Structure

part3-datawarehouse/
├── README.md
├── star_schema_design.md
├── warehouse_schema.sql
├── warehouse_data.sql
└── analytics_queries.sql


---

## 1. Star Schema Design

**File:** `star_schema_design.md`

The data warehouse follows a **Star Schema**, consisting of one central fact table connected to multiple dimension tables.

### Fact Table: `fact_sales`

- **Grain:** One row per product per order line item  
- **Business Process:** Sales transactions  

**Measures stored in the fact table:**
- quantity_sold – Number of units sold  
- unit_price – Price per unit at the time of sale  
- discount_amount – Discount applied on the sale  
- total_amount – Final sales amount (quantity × unit_price − discount)  

**Foreign Keys:**
- date_key → dim_date  
- product_key → dim_product  
- customer_key → dim_customer  

---

### Dimension Tables

#### `dim_date`
This table supports time-based analysis such as daily, monthly, quarterly, and yearly reporting.

Attributes include:
- date_key (YYYYMMDD surrogate key)  
- full_date  
- day_of_week  
- day_of_month  
- month, month_name  
- quarter  
- year  
- is_weekend  

#### `dim_product`
This table stores descriptive information about products.

Attributes include:
- product_key (surrogate key)  
- product_id (business identifier)  
- product_name  
- category  
- subcategory  
- unit_price  

#### `dim_customer`
This table stores customer-related information used for analysis and segmentation.

Attributes include:
- customer_key (surrogate key)  
- customer_id (business identifier)  
- customer_name  
- city  
- state  
- customer_segment  

---

## 2. Design Rationale

The star schema is designed at the **transaction line-item level**, meaning each record in the fact table represents one product sold in a transaction. This level of detail allows accurate analysis at product, customer, and time levels.

**Surrogate keys** are used for all dimension tables to improve query performance and to avoid dependency on business keys that may change over time. This also keeps the warehouse design stable and consistent.

Separating facts and dimensions makes it easy to perform **drill-down and roll-up operations**, such as analyzing sales from year to quarter to month or from product category to individual products.

---

## 3. Data Warehouse Schema Implementation

**File:** `warehouse_schema.sql`

This file creates the data warehouse schema in the database:


The following tables are created:
- dim_date  
- dim_product  
- dim_customer  
- fact_sales  

Foreign key constraints are used in the fact table to maintain referential integrity with the dimension tables.

---

## 4. Data Population

**File:** `warehouse_data.sql`

This file inserts dummy data into the data warehouse as per assignment requirements.

### Data Volume
- dim_date: 30 records (January–February 2024)  
- dim_product: 15 products across 3 categories  
- dim_customer: 12 customers across 4 cities  
- fact_sales: 40 sales transactions  

### Data Characteristics
- Includes both weekdays and weekends  
- Products have varied price ranges  
- Customers belong to different cities and states  
- Sales data reflects realistic quantities and revenue patterns  

All foreign key references are valid and consistent with the schema.

---

## 5. OLAP Analytics Queries

**File:** `analytics_queries.sql`

This file contains analytical SQL queries written on the star schema.

### Query 1: Monthly Sales Drill-Down
- Shows sales broken down by **Year → Quarter → Month**
- Displays total sales and total quantity sold for 2024  

### Query 2: Product Performance Analysis
- Identifies the top 10 products based on revenue  
- Calculates total units sold and revenue contribution percentage  

### Query 3: Customer Segmentation Analysis
- Segments customers into **High Value, Medium Value, and Low Value** groups  
- Displays customer count, total revenue, and average revenue per segment  

These queries demonstrate how the data warehouse supports analytical reporting.

---

## 6. How to Run Part 3

### Step 1: Create Database
```sql
CREATE DATABASE fleximart_dw;
USE fleximart_dw;

Step 2: Create Warehouse Schema
mysql -u root -p fleximart_dw < warehouse_schema.sql

Step 3: Load Warehouse Data
mysql -u root -p fleximart_dw < warehouse_data.sql

Step 4: Run Analytics Queries
mysql -u root -p fleximart_dw < analytics_queries.sql

7. Analytical Capabilities

This data warehouse enables the following analytical capabilities:

Time-based sales analysis using the date dimension

Product and category-level performance comparison

Revenue contribution analysis

Customer segmentation based on spending behavior

Drill-down and roll-up analysis across dimensions

These capabilities help in understanding business performance and trends.

8. Conclusion

This part of the project successfully implements a complete data warehouse for FLEXIMART. The star schema design, structured data loading, and analytical queries together provide a solid foundation for business intelligence and meet all the requirements of the assignment.