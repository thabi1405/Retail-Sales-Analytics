import pandas as pd
import matplotlib.pyplot as plt
from data_cleaning import load_and_clean_data
from analysis import category_analysis

df = load_and_clean_data("data/samplesuperstore.csv")

print("===== DATASET INFORMATION =====")
print(df.info())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

print("\n===== DATE CONVERSION =====")
print(df[["Order Date", "Ship Date"]].dtypes)

print("\n===== NEW COLUMNS =====")
print(df[["Year", "Month", "Month Name", "Shipping Days"]].head())

# =====================================
# BUSINESS QUESTION 1
# Which category generates the highest sales and profit?
# =====================================

category_summary = category_analysis(df)

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

# ======================================
# BUSINESS QUESTION 3
# Which month generates the highest sales and profit?
# ======================================

monthly_summary = (
    df.groupby("Month Name")[["Sales", "Profit"]]
      .sum()
)

# Put the months in calendar order
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_summary = monthly_summary.reindex(month_order)

print("\n===== SALES & PROFIT BY MONTH =====")
print(monthly_summary.round(2))

# ======================================
# CHART 3
# Monthly Sales Trend
# ======================================

monthly_summary["Sales"].plot(
    kind="line",
    figsize=(12, 6),
    marker="o",
    linewidth=3,
    title="Monthly Sales Trend"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

plt.savefig("outputs/charts/monthly_sales_trend.png")
plt.close()

print("\n✓ Monthly sales chart saved!")

# ======================================
# BUSINESS QUESTION 4
# Which customer segment generates the most revenue and profit?
# ======================================

segment_summary = (
    df.groupby("Segment")[["Sales", "Profit"]]
      .sum()
      .sort_values(by="Profit", ascending=False)
)

print("\n===== SALES & PROFIT BY SEGMENT =====")
print(segment_summary.round(2))

# ======================================
# CHART 4
# Profit by Customer Segment
# ======================================

segment_summary["Profit"].plot(
    kind="bar",
    figsize=(8,5),
    title="Profit by Customer Segment"
)

plt.xlabel("Customer Segment")
plt.ylabel("Profit")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("outputs/charts/profit_by_segment.png")
plt.close()

print("✓ Customer segment chart saved!")

# ======================================
# BUSINESS QUESTION 5
# Which regions are underperforming?
# ======================================

region_summary = (
    df.groupby("Region")[["Sales", "Profit"]]
      .sum()
      .sort_values(by="Profit", ascending=False)
)

print("\n===== SALES & PROFIT BY REGION =====")
print(region_summary.round(2))

# ======================================
# CHART 5
# Profit by Region
# ======================================

region_summary["Profit"].plot(
    kind="bar",
    figsize=(8,5),
    title="Profit by Region"
)

plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("outputs/charts/profit_by_region.png")
plt.close()

print("✓ Region chart saved!")

# ======================================
# BUSINESS QUESTION 6
# Are discounts helping or hurting profit?
# ======================================

discount_summary = (
    df.groupby("Discount")[["Sales", "Profit"]]
      .sum()
      .sort_values(by="Discount")
)

print("\n===== SALES & PROFIT BY DISCOUNT =====")
print(discount_summary.round(2))

# ======================================
# CHART 6
# Discount vs Profit
# ======================================

plt.figure(figsize=(10,6))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.grid(True)

plt.tight_layout()

plt.savefig("outputs/charts/discount_vs_profit.png")
plt.close()

print("✓ Discount vs Profit chart saved!")

# ======================================
# BUSINESS QUESTION 7
# Top 10 Customers by Sales
# ======================================

top_customers = (
    df.groupby("Customer Name")[["Sales", "Profit"]]
      .sum()
      .sort_values(by="Sales", ascending=False)
      .head(10)
)

print("\n===== TOP 10 CUSTOMERS =====")
print(top_customers.round(2))

# ======================================
# CHART 7
# Top 10 Customers by Sales
# ======================================

top_customers["Sales"].plot(
    kind="bar",
    figsize=(12,6),
    title="Top 10 Customers by Sales"
)

plt.xlabel("Customer")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("outputs/charts/top_10_customers.png")
plt.close()

print("✓ Top customers chart saved!")

# ======================================
# BUSINESS QUESTION 8
# How is total sales distributed across product categories?
# ======================================

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== SALES CONTRIBUTION BY CATEGORY =====")
print(category_sales.round(2))

# ======================================
# CHART 8
# Sales Contribution by Category
# ======================================

plt.figure(figsize=(8,8))

plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Contribution by Category")

plt.tight_layout()

plt.savefig("outputs/charts/category_sales_pie.png")
plt.close()

print("✓ Category sales pie chart saved!")

# ======================================
# BUSINESS QUESTION 9
# Which products generate the highest profit?
# ======================================

top_products = (
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== TOP 10 MOST PROFITABLE PRODUCTS =====")
print(top_products.round(2))

# ======================================
# CHART 9
# Top 10 Most Profitable Products
# ======================================

top_products.plot(
    kind="barh",
    figsize=(12,7),
    title="Top 10 Most Profitable Products"
)

plt.xlabel("Profit")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig("outputs/charts/top_profitable_products.png")
plt.close()

print("✓ Top profitable products chart saved!")

# ======================================
# BUSINESS QUESTION 10
# Which products generate the biggest losses?
# ======================================

worst_products = (
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values(ascending=True)
      .head(10)
)

print("\n===== TOP 10 LEAST PROFITABLE PRODUCTS =====")
print(worst_products.round(2))

# ======================================
# CHART 10
# Top 10 Least Profitable Products
# ======================================

worst_products.plot(
    kind="barh",
    figsize=(12,7),
    title="Top 10 Least Profitable Products"
)

plt.xlabel("Profit")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig("outputs/charts/least_profitable_products.png")
plt.close()

print("✓ Least profitable products chart saved!")