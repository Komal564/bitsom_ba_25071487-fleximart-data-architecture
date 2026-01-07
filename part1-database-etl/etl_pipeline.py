import pandas as pd
import numpy as np
print("succes")
import mysql.connector
print("connected")
print ("all libraries working")
print("mysql connected succesfully")
db_conn = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "KO@Mal!2006",
     database = "FLEXIMART_DATA"
 )
cursor = db_conn.cursor()

print("mysql conncted succesfully")

import os
print(os.getcwd())
   
import pandas as pd

# #Path of csv
customers_path = "data_set/customers_raw (1).csv"

# #Read csv
customers_df = pd.read_csv(customers_path)
records_processed =len(customers_df)
print("customers_df - records_processed:", records_processed)
  
# # TOP 5 rows
print(customers_df.head())

# #total number of records
("\nTotal number of records:",len(customers_df))

# #===================================================
# #TRANSFORM STEP 1:REMOVE GARBAGE ROWS 
# #===================================================

# #Customer_id null rows remove
customers_df = customers_df[customers_df['customer_id'].notna()]

print("\nAfter removing garbage rows:")
print("recordds:",len(customers_df))

# # ============================================
# # TRANSFORM STEP 3: Phone number as string
# # ============================================

customers_df['phone'] = customers_df['phone'].astype(str)

print("\nPhone column converted to string")
print(customers_df['phone'].head())


# # ============================================
# # TRANSFORM STEP 4: Clean & standardize phone numbers
# # ============================================
import re
import pandas as pd
import re
import pandas as pd

def standardize_phone(phone):
    if pd.isna(phone):
        return ""
    phone = str(phone)   

    digits = re.sub(r'\D', '', (phone))

    if len(digits) >= 10:
        clean_number = digits[-10:]
        return "+91 " + clean_number   # space also added
    else:
        return ""

customers_df['phone'] = customers_df['phone'].apply(standardize_phone)

# IMPORTANT: force phone column as string
customers_df['phone'] = customers_df['phone'].astype(str)
print(customers_df['phone'].head(10))

# ============================================
#check emails
def is_valid_email(email):
    if pd.isna(email):
        return False
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, str(email)))

customers_df['email_valid'] = customers_df['email'].apply(is_valid_email)

print(customers_df[['email', 'email_valid']].head())

print("Invalid emails count:", (~customers_df['email_valid']).sum())

# TRANSFORM STEP 7: Handle missing emails
# ============================================
def generate_email(row):
    if pd.isna(row['email']) or row['email'].strip() == "":
        return f"{row['first_name']}.{row['last_name']}.{row['customer_id']}@fleximart.com".lower()
    else:
        return row['email'].strip().lower()


customers_df['email'] = customers_df.apply(generate_email, axis=1)

print("\nEmails after handling missing values:")
print(customers_df[['customer_id', 'email']].head(10))


print("\nCustomer IDs sample:")
print(customers_df['customer_id'].head(10))


print("\nUnique customer_id count:",
      customers_df['customer_id'].nunique())

print("Total rows:",
      len(customers_df))


print("\nPhone format check:")
print(customers_df['phone'].unique()[:5])


print("\nMissing emails count:",
      customers_df['email'].isna().sum())

print("Duplicate emails count:",
      customers_df['email'].duplicated().sum())

#============================================

# FINAL TRANSFORM: Remove duplicate customers by customer_id
#========================================

before = len(customers_df)

customers_df = customers_df.drop_duplicates(subset='customer_id',keep='first')

after = len(customers_df)

print("\nFinal duplicate customers removed:",before-after)
print("final customers records:",after)

print("\nFINAL CHECK")
print("Total rows:",len(customers_df))
print("unique customer_id:",customers_df["customer_id"].nunique())
print("Duplicate emails:",customers_df["email"].duplicated().sum())

# =============================
# TRANSFORM STEP:
# Robust registration_date cleaning
# =============================

def clean_registration_date(date_value):
    try:
        # Try parsing date normally
        parsed_date = pd.to_datetime(date_value, dayfirst=True)
        return parsed_date.strftime('%Y-%m-%d')
    except:
        # If parsing fails, assign default date
        return '2000-01-01'


# Apply cleaning function
customers_df['registration_date'] = customers_df['registration_date'].apply(
    clean_registration_date
)

#final verification
print("\nRegistration dates after final cleaning:")
print(customers_df["registration_date"].head())

# =================================================
import pandas as pd
import os
# TRANSFORM STEP: Clean city coulmns 1
customers_df.columns = customers_df.columns.str.strip().str.lower()

# Clean city names 2
customers_df['city'] = (
    customers_df['city']
    .astype(str)
    .str.strip()
    .str.title()
)

# Final city verification
# =====================================================

print("\nUnique cities after final cleaning:")
print(sorted(customers_df['city'].unique()))

print("\nCleaned customers sample:")
print(customers_df)

# =====================================================
# SAVE CLEAN CUSTOMERS CSV
# =====================================================

import os
os.makedirs("data", exist_ok=True)
customers_clean_path = "data/customers_clean.csv"
customers_df.to_csv(customers_clean_path, index=False)

print("Clean customers data saved at:", customers_clean_path)

#============================
import pandas as pd
# =====================================================
# PRODUCTS ETL – STARTING FROM PATH
# =====================================================

import pandas as pd
import os

#Confirm current working directory
print("Running from:", os.getcwd())

# base data folder
DATA_PATH = "data_set"

# products file path
products_file = os.path.join(DATA_PATH, "products_raw.csv")

#  file exists 
if not os.path.exists(products_file):
    raise FileNotFoundError(f"Products file not found at: {products_file}")

# Read products CSV
products_df = pd.read_csv(products_file)

#  Basic verification
print("Products file loaded successfully")
print("Total product records:", len(products_df))
print(products_df.head())
print("Total records:",len(products_df))
# ================================
# CLEAN CATEGORY NAMES
# ================================
products_df['category'] = (
    products_df['category']
    .str.strip()
    .str.lower()
)

category_mapping = {
    'electronics': 'Electronics',
    'fashion': 'Fashion',
    'groceries': 'Groceries'
}

products_df['category'] = products_df['category'].map(category_mapping)
products_df['category'] = products_df['category'].fillna('unknown')
print("\nUnique categories after cleaning:")
print(products_df['category'].unique())


# ================================
# CLEAN PRODUCT NAMES
# ================================
products_df['product_name'] = (
    products_df['product_name']
    .astype(str)
    .str.strip()
)
print("\nSample cleaned product names:")
print(products_df['category'].head())

# ================================
# FIX MISSING STOCK
# ================================
products_df['stock_quantity'] = (
    products_df['stock_quantity']
    .fillna(0)
    .astype(int)
)
print("Missing stock after fix:", products_df['stock_quantity'].isna().sum())

# ================================
# FIX MISSING PRICES
# (Category-wise average)
# ================================
products_df['price'] = products_df['price'].astype(float)

products_df['price'] = products_df.groupby('category')['price']\
    .transform(lambda x: x.fillna(x.median()))
products_df['price'] = products_df['price'].fillna(products_df['price'].median())
print("Missing prices after fix:", products_df['price'].isna().sum())

# ================================
# FINAL SORTING
# ================================
products_df = products_df.sort_values(by='product_id').reset_index(drop=True)

# ================================
# FINAL CHECK
# ================================
print(" Cleaned & Sorted Products Data\n")
print(products_df)

print("\n Missing values check:")
print(products_df.isnull().sum())

#====================
#final verification
#====================
print("\nCleaned products sample:")

# =====================================================
# STEP 6: SAVE CLEAN PRODUCTS CSV
# =====================================================
products_clean_path = "data/products_clean.csv"
products_df.to_csv(products_clean_path, index=False)

print("Clean products data saved at:")
print(products_clean_path)

# ============================================
# SALES ETL - STEP 1: EXTRACT
# =====================================================

import pandas as pd

sales_csv_path = r"C:\Users\Dell\OneDrive\Desktop\FLEXIMART\data_set\sales_raw.csv"

sales_df = pd.read_csv(sales_csv_path)

print("\n================ SALES RAW DATA ================\n")
print(sales_df.head())

print("\nTotal sales records:", len(sales_df))

# ==============================
# DEBUG
# ==============================

print("\nSales DataFrame info:")
print(sales_df.info())

print("\nLast 5 rows of sales data:")
print(sales_df.tail())

# ==============================
# SALES TRANSFORM: Remove garbage rows
# ==============================

before = len(sales_df)

sales_df = sales_df[sales_df['transaction_id'].notna()]

after = len(sales_df)

print("\nGarbage sales rows removed:", before - after)
print("Sales records after garbage removal:", after)

# ==============================
# SALES TRANSFORM: Remove duplicate transactions
# ==============================

before = len(sales_df)

sales_df = sales_df.drop_duplicates(subset='transaction_id', keep='first')

after = len(sales_df)

print("\nDuplicate transactions removed:", before - after)
print("Sales records after deduplication:", after)

# ==============================
# SALES TRANSFORM: Drop rows with missing customer_id
# ==============================

before = len(sales_df)

sales_df = sales_df[sales_df['customer_id'].notna()]

after = len(sales_df)

print("\nRows dropped due to missing customer_id:", before - after)
print("Sales records after customer_id cleaning:", after)

# ==============================
# SALES TRANSFORM: Drop rows with missing product_id
# ==============================

before = len(sales_df)

sales_df = sales_df[sales_df['product_id'].notna()]

after = len(sales_df)

print("\nRows dropped due to missing product_id:", before - after)
print("Sales records after product_id cleaning:", after)

# ==============================
# SALES TRANSFORM: Clean transaction_date
# ==============================

def clean_transaction_date(date_value):
    try:
        parsed_date = pd.to_datetime(date_value, dayfirst=True)
        return parsed_date.strftime('%Y-%m-%d')
    except:
        return None

sales_df['transaction_date'] = sales_df['transaction_date'].apply(clean_transaction_date)

print("\nInvalid transaction dates after cleaning:",
      sales_df['transaction_date'].isna().sum())

# ==============================
# STRICT FK CLEANING: Remove empty strings also
# ==============================

sales_df['customer_id'] = sales_df['customer_id'].astype(str).str.strip()
sales_df['product_id'] = sales_df['product_id'].astype(str).str.strip()

before = len(sales_df)

sales_df = sales_df[
    (sales_df['customer_id'] != '') &
    (sales_df['product_id'] != '')
]

after = len(sales_df)

print("\nRows dropped due to empty customer_id/product_id:", before - after)
print("Sales records after strict FK cleaning:", after)

# =====================================================
# SALES TRANSFORM: Add total_amount column
# =====================================================

sales_df['total_amount'] = sales_df['quantity'] * sales_df['unit_price']

print("\nTotal amount column added.")
print(sales_df[['transaction_id', 'quantity', 'unit_price', 'total_amount']].head())

print("\nNULL check including total_amount:")
print(
    sales_df[
        ['transaction_id','customer_id','product_id',
         'quantity','unit_price','total_amount','transaction_date']
    ].isna().sum()
)

print("\nTotal amount sanity (min, max):")
print(sales_df['total_amount'].min(), sales_df['total_amount'].max())


print("\nCleaned sales sample:")
# =====================================================
# SAVE CLEAN SALES CSV
# =====================================================
import os
os.makedirs("/Data",exist_ok= True)
sales_clean_path = "data/sales_clean.csv"

sales_df.to_csv(sales_clean_path, index=False )
print("Clean sales data saved to:")
print(sales_clean_path)

# #====================================================
# #LOAD PHASE: INSERT CUSTOMERS
# #====================================================

# insert_customer_sql = """
# INSERT IGNORE INTO customers
# (first_name, last_name, email, phone, city, registration_date)
# VALUES (%s, %s, %s, %s, %s, %s)
# """

# customer_records = customers_df[
#    ['first_name', 'last_name', 'email', 'phone', 'city', 'registration_date']
# ].values.tolist()

# cursor.executemany(insert_customer_sql, customer_records)
# db_conn.commit()

# print(f" Customers inserted: {cursor.rowcount}")

# # =====================================================
# # LOAD PHASE: INSERT PRODUCTS
# # =====================================================

# insert_product_sql = """
# INSERT INTO products
# (product_name, category, price, stock_quantity)
# VALUES (%s, %s, %s, %s)
# """

# product_records = products_df[
#    ['product_name', 'category', 'price', 'stock_quantity']
# ].values.tolist()

# cursor.executemany(insert_product_sql, product_records)
# db_conn.commit()

# print(f" Products inserted: {cursor.rowcount}")

# cursor = db_conn.cursor()
# print(" MySQL connection successful")

# # =====================================================

# =====================================================
# BUILD PRODUCT MAP (CSV product_id -> DB product_id)
#=====================================================

# Get DB products
cursor.execute("SELECT product_id, product_name FROM products")
db_products = cursor.fetchall()

# Build CSV lookup: product_id -> product_name
csv_product_lookup = {
    row["product_id"]: row["product_name"]
    for _, row in products_df.iterrows()
}

product_map = {}

for db_pid, db_name in db_products:
    for csv_pid, csv_name in csv_product_lookup.items():
        if csv_name.strip().lower() == db_name.strip().lower():
            product_map[csv_pid] = db_pid

print(" Product map created:", len(product_map))


# =====================================================
# BUILD CUSTOMER MAP (email -> db customer_id)
# =====================================================

cursor.execute("SELECT customer_id, email FROM customers")
customer_map = {email: cid for cid, email in cursor.fetchall()}

print(" Customer map created:", len(customer_map))


# =====================================================
# CSV customer_id -> email lookup
# =====================================================

customer_lookup = {
    row["customer_id"]: row["email"]
    for _, row in customers_df.iterrows()
}

print(" Customer lookup created")


# =====================================================
# DETECT TOTAL AMOUNT COLUMN SAFELY
# =====================================================

if "total_amount" in sales_df.columns:
    amount_col = "total_amount"
elif "amount" in sales_df.columns:
    amount_col = "amount"
elif "order_amount" in sales_df.columns:
    amount_col = "order_amount"
else:
    raise Exception(
        f"No amount column found. Available columns: {list(sales_df.columns)}"
    )

print(f" Using amount column: {amount_col}")


# =====================================================
# INSERT ORDERS & BUILD ORDER MAP
# =====================================================

insert_order_sql = """
INSERT INTO orders (customer_id, order_date, total_amount)
VALUES (%s, %s, %s)
"""

order_map = {}
inserted = 0
skipped = 0


for _, row in sales_df.iterrows():

    # CSV customer_id -> email
    email = customer_lookup.get(row["customer_id"])
    if email is None:
        skipped += 1
        continue

    # email -> DB customer_id
    db_customer_id = customer_map.get(email)
    if db_customer_id is None:
        skipped += 1
        continue

    cursor.execute(
        insert_order_sql,
        (
            db_customer_id,
            row["transaction_date"],
            row[amount_col]
        )
    )

    order_id = cursor.lastrowid
    order_map[row["transaction_id"]] = order_id

    inserted += 1

db_conn.commit()

print(f" Orders inserted: {inserted}")
print(f" Orders skipped: {skipped}")

# =====================================================
# INSERT ORDER ITEMS
# =====================================================

insert_order_item_sql = """
INSERT INTO order_items
(order_id, product_id, quantity, unit_price, subtotal)
VALUES (%s, %s, %s, %s, %s)
"""


inserted_items = 0
skipped_items = 0

for _, row in sales_df.iterrows():

    order_id = order_map.get(row["transaction_id"])
    if order_id is None:
        skipped_items += 1
        continue

    product_id = product_map.get(row["product_id"])
    if product_id is None:
        skipped_items += 1
        continue
    
    subtotal = int(row["quantity"]) * float(row["unit_price"])

    cursor.execute(
        insert_order_item_sql,
        (
            order_id,
            product_id,
            int(row["quantity"]),
            float(row["unit_price"]),
            subtotal
        )
    )

    inserted_items += 1

db_conn.commit()

print(f" Order items inserted: {inserted_items}")
print(f" Order items skipped: {skipped_items}")


# ===============================
# CLOSE CONNECTION
# ===============================

cursor.close()
db_conn.close()
print(" Database connection closed")
#===============================











