import pandas as pd

# Load dataset
df = pd.read_csv("data/SampleSuperstore.csv")

print("===== DATASET INFORMATION =====")
print(df.info())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

# =====================================
# DATA CLEANING
# =====================================

# Convert date columns to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\n===== DATE CONVERSION =====")
print(df[["Order Date", "Ship Date"]].dtypes)

# =====================================
# FEATURE ENGINEERING
# =====================================

# Create new date-related columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()

# Calculate shipping time
df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

print("\n===== NEW COLUMNS =====")
print(df[["Year", "Month", "Month Name", "Shipping Days"]].head())

# =====================================
# BUSINESS QUESTION 1
# Which category generates the highest sales and profit?
# =====================================

category_summary = (
    df.groupby("Category")[["Sales", "Profit"]]
      .sum()
      .sort_values(by="Profit", ascending=False)
)

print("\n===== SALES & PROFIT BY CATEGORY =====")
print(category_summary.round(2))

import matplotlib.pyplot as plt

category_summary["Profit"].plot(
    kind="bar",
    figsize=(8,5),
    title="Profit by Category"
)

plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()

plt.savefig("outputs/charts/profit_by_category.png")
plt.close()

# =====================================
# BUSINESS QUESTION 2
# Which sub-category makes the most profit?
# =====================================

subcategory_summary = (
    df.groupby("Sub-Category")[["Sales", "Profit"]]
      .sum()
      .sort_values(by="Profit", ascending=False)
)

print("\n===== SALES & PROFIT BY SUB-CATEGORY =====")
print(subcategory_summary.round(2))

# =====================================
# CHART 2
# Profit by Sub-Category
# =====================================

subcategory_summary["Profit"].plot(
    kind="bar",
    figsize=(12, 6),
    title="Profit by Sub-Category"
)

plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/charts/profit_by_subcategory.png")
plt.close()