# Import necessary libraries
import pandas as pd
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent   # folder containing your .py files

RAW_DATA_DIR = PROJECT_ROOT / "raw_data"
CLEANED_DATA_DIR = PROJECT_ROOT / "cleaned_data"


# Load the cleaned CSV file
df = pd.read_csv(CLEANED_DATA_DIR / 'flour4four_orders_cleaned.csv')

# create dimension table for business
dim_business = df[[
    "business_id",
    "business_name",
    "business_type",
    "business_address",
    "contact_name",
    "contact_phone"
]].drop_duplicates(subset="business_id").reset_index(drop=True)

# create dimension table for rider
dim_rider = df[[
    "rider_name",
    "rider_phone"
]].drop_duplicates().reset_index(drop=True)
dim_rider["rider_id"] = range(1, len(dim_rider) + 1)
dim_rider = dim_rider[["rider_id","rider_name","rider_phone"]]

# create dimension table for flour type
dim_flour = df[["flour_type"]].drop_duplicates().reset_index(drop=True)
dim_flour["flour_type_id"] = range(1, len(dim_flour) + 1)
dim_flour = dim_flour[["flour_type_id","flour_type"]]

fact_orders = df.copy()

# Merge to add flour_type_id
fact_orders = fact_orders.merge(dim_flour, on="flour_type", how="left") \
    .merge(dim_rider, on=["rider_name", "rider_phone"], how="left") \
        [["order_id","order_date","delivery_date","business_id","rider_id","flour_type_id","quantity_bags","price_per_bag","total_amount","payment_method","order_status"]]

# Export dimension and fact tables to CSV
dim_business.to_csv(CLEANED_DATA_DIR / 'dim_business.csv', index=False)
dim_flour.to_csv(CLEANED_DATA_DIR / 'dim_flour.csv', index=False)
dim_rider.to_csv(CLEANED_DATA_DIR / 'dim_rider.csv', index=False)
fact_orders.to_csv(CLEANED_DATA_DIR / 'fact_orders.csv', index=False)

print("✔ All dataframes exported to CSV successfully!")