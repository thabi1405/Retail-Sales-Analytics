import os
import sys
import sqlite3

# Add the project root to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_cleaning import load_and_clean_data

# Load the cleaned dataset
df = load_and_clean_data("data/samplesuperstore.csv")

# Create SQLite database
conn = sqlite3.connect("sql/retail_sales.db")

# Save the cleaned dataframe
df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print(" SQLite database updated successfully!")