# FlexiMart Data Architecture Project

**Student Name:** Komal Kaur  
**Student ID :** bitsom_ba_25071487 
**Email:** Komalkaurladhar@gmail.com
**Date:** 01/07/2026

----

### Project Overview

The Fleximart Data Engineering & Analytics Project is an end-to-end data solution designed to demonstrate real-world ETL processing, Data Warehousing, Analytics, and NoSQL integration.

The project integrates:

A Python-based ETL pipeline

A SQL Data Warehouse using Star Schema

Business & analytical SQL queries

MongoDB (NoSQL) for semi-structured product catalog analysis

Data quality validation and documentation


### Overall Architecture

Raw Data (CSV / JSON)
        ↓
Python ETL Pipeline
        ↓
Cleaned Data
        ↓
SQL Data Warehouse (Star Schema)
        ↓
Analytics & Business Queries


### Additionally:

Product catalog data is analyzed using MongoDB for NoSQL use cases.

Project Structure : Both of them can be considered.

FLEXIMART/
│
├── data/
│   ├── customers_clean.csv
│   ├── products_clean.csv
│   └── sales_clean.csv
│
├── data_set/
│   ├── customers_raw(1).csv
│   ├── products_raw.csv
│   └── sales_raw.csv
│
├── part1-database-etl/
│   ├── etl_pipeline.py
│   ├── schema_documentation.md
│   ├── business_queries.sql
│   ├── data_quality_report.txt
│   ├── requirements.txt
│   └── README1.md
│
├── part2-nosql/
│   ├── nosql_analysis.md
│   ├── mongodb_operations.py
│   ├── mongodb_operations.js 1
│   ├── products_catalog.json
│   ├── requirements.txt
│   └── README2.md
│
├── part3-datawarehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   ├── analytics_queries.sql
│   └── README3.md
│
├── .gitignore
|──root-README.md

### ETL Pipeline

Main File: etl_pipeline.py

The ETL pipeline performs the following steps:

1. Extraction

Reads raw data related to:

Customers

Products

Sales transactions

2. Transformation

Handles missing values

Removes duplicates

Standardizes data formats

Applies data cleaning rules

3. Loading

Writes cleaned data for warehouse loading

Prepares data for analytical querying

The ETL process ensures data consistency, accuracy, and analytics readiness.

### Data Warehouse Design

The SQL Data Warehouse is designed using a Star Schema architecture:

Fact Table

Sales fact table containing transactional metrics

Dimension Tables

Customer Dimension

Product Dimension

Time Dimension

Detailed documentation is available in:

schema_documentation.md

star_schema_design.md

### Analytics & Business Queries

The project includes SQL queries to answer key business and analytical questions, such as:

Sales trends over time

Top-performing products

Customer purchase behavior

Revenue analysis

### Key Files:

analytics_queries.sql

business_queries.sql

###  NoSQL (MongoDB) Component

To demonstrate NoSQL capabilities, the project includes MongoDB-based analysis:

Product catalog stored as JSON

Flexible schema for semi-structured data

MongoDB operations implemented using:

JavaScript (mongodb_operations.js 1)

Python (mongodb_operations.py)

### This component highlights:

Schema-less data handling

NoSQL querying and analysis

### Data Quality Validation

Data quality checks are documented in:

data_quality_report.txt

### Checks include:

Missing value detection

Duplicate record identification

Data type validation

Basic consistency checks

### Setup & Installation

1. Clone the Repository
git clone <repository-url>
cd Fleximart

2. Install Dependencies
pip install -r Requirement.txt

3. Configure Databases

Configure SQL database connection (MySQL or compatible)

Configure MongoDB connection

4. Run ETL Pipeline
python etl_pipeline.py

5. Create Warehouse & Run Queries

Execute warehouse_schema.sql

Load data using warehouse_data.sql

Run analytics and business queries

###  Technologies Used

Python – ETL and data processing

SQL (MySQL) – Data warehouse and analytics

MongoDB – NoSQL data analysis

Pandas – Data transformation

VS Code – Development environment

###  Key Learning Outcomes

End-to-end ETL pipeline implementation

Dimensional modeling using Star Schema

SQL-based analytics and reporting

NoSQL data handling with MongoDB

Data quality assessment and validation

### Challenges Faced :
Handling inconsistent raw data formats.

Designing a proper star schema

Understanding Foreign key relationship

Running and verifiying analytical queries

These chanllenges helped in better understanding of data architecture concepts

### Conclusion 

This project demonstrates an end to end data architecture solution from raw data upload to advance analytics. 

This design practices industry practices and fulfills all assignment requirements.

