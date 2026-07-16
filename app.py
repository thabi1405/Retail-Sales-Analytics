import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_cleaning import load_and_clean_data

# PAGE CONFIGURATION

st.set_page_config(
    page_title="Retail Sales Analytics Dashboard",
    page_icon="",
    layout="wide"
)

# SIDEBAR

st.sidebar.title(" Retail Dashboard")

st.sidebar.markdown("""
### Navigation

Use the filters below to explore the data.

---

Developed by

**Rethabile Mmako**
""")

# TITLE

st.title(" Retail Sales Analytics Dashboard")

st.markdown("""
This dashboard analyzes Superstore retail sales data to identify:

- Sales trends
- Customer behavior
- Product profitability
- Regional performance
- Business insights
""")

# LOAD DATA

df = load_and_clean_data("data/samplesuperstore.csv")

# FILTERS

st.sidebar.header("Filters")

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique()),
    key="region_filter"
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique()),
    key="category_filter"
)

selected_segment = st.sidebar.multiselect(
    "Select Customer Segment",
    options=sorted(df["Segment"].unique()),
    default=sorted(df["Segment"].unique()),
    key="segment_filter"
)

selected_year = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique()),
    key="year_filter"
)

# APPLY FILTERS

df = df[
    (df["Region"].isin(selected_region)) &
    (df["Category"].isin(selected_category)) &
    (df["Segment"].isin(selected_segment)) &
    (df["Year"].isin(selected_year))
]

# KPI CARDS

st.subheader(" Executive Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    " Total Sales",
    f"${df['Sales'].sum():,.2f}"
)

col2.metric(
    " Total Profit",
    f"${df['Profit'].sum():,.2f}"
)

col3.metric(
    " Total Orders",
    f"{len(df):,}"
)

st.info(
    f"""
Average Order Value: ${df['Sales'].mean():,.2f}

Average Profit per Order: ${df['Profit'].mean():,.2f}
"""
)

st.caption(
    f"Displaying {len(df):,} records based on the selected filters."
)

st.write("---")

# DATASET PREVIEW

with st.expander(" View Dataset Preview"):
    st.dataframe(df.head())

# DATA FOR VISUALIZATIONS

monthly_sales = (
    df.groupby("Month Name")["Sales"]
    .sum()
    .reindex([
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])
    .reset_index()
)

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .reset_index()
)

segment_profit = (
    df.groupby("Segment")["Profit"]
    .sum()
    .reset_index()
)

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

top_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

least_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
    .head(10)
    .reset_index()
)

# PLOTLY CHARTS

fig_monthly = px.line(
    monthly_sales,
    x="Month Name",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)
fig_monthly.update_layout(height=350, title_x=0.5)

fig_category = px.bar(
    category_profit,
    x="Category",
    y="Profit",
    color="Category",
    title="Profit by Category"
)
fig_category.update_layout(height=350, title_x=0.5)

fig_subcategory = px.bar(
    subcategory_profit,
    x="Sub-Category",
    y="Profit",
    title="Profit by Sub-Category"
)
fig_subcategory.update_layout(height=350, title_x=0.5)

fig_region = px.bar(
    region_profit,
    x="Region",
    y="Profit",
    color="Region",
    title="Profit by Region"
)
fig_region.update_layout(height=350, title_x=0.5)

fig_segment = px.bar(
    segment_profit,
    x="Segment",
    y="Profit",
    color="Segment",
    title="Profit by Customer Segment"
)
fig_segment.update_layout(height=350, title_x=0.5)

fig_discount = px.scatter(
    df,
    x="Discount",
    y="Profit",
    color="Category",
    title="Discount vs Profit"
)
fig_discount.update_layout(height=350, title_x=0.5)

fig_category_pie = px.pie(
    df,
    names="Category",
    values="Sales",
    title="Category Sales Contribution"
)
fig_category_pie.update_layout(height=350, title_x=0.5)

fig_customers = px.bar(
    top_customers,
    x="Customer Name",
    y="Sales",
    title="Top 10 Customers"
)
fig_customers.update_layout(height=350, title_x=0.5)

fig_top_products = px.bar(
    top_products,
    x="Profit",
    y="Product Name",
    orientation="h",
    title="Top 10 Most Profitable Products"
)
fig_top_products.update_layout(height=350, title_x=0.5)

fig_least_products = px.bar(
    least_products,
    x="Profit",
    y="Product Name",
    orientation="h",
    title="Top 10 Least Profitable Products"
)
fig_least_products.update_layout(height=350, title_x=0.5)

# DASHBOARD TABS

tab1, tab2, tab3 = st.tabs([
    " Sales Analysis",
    " Customer Analysis",
    " Product Analysis"
])

# SALES ANALYSIS

with tab1:

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_monthly, use_container_width=True)
        st.plotly_chart(fig_region, use_container_width=True)
        st.plotly_chart(fig_category_pie, use_container_width=True)

    with col2:
        st.plotly_chart(fig_category, use_container_width=True)
        st.plotly_chart(fig_discount, use_container_width=True)

# CUSTOMER ANALYSIS

with tab2:

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_segment, use_container_width=True)

    with col2:
        st.plotly_chart(fig_customers, use_container_width=True)

# PRODUCT ANALYSIS

with tab3:

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_subcategory, use_container_width=True)

    with col2:
        st.plotly_chart(fig_top_products, use_container_width=True)
        st.plotly_chart(fig_least_products, use_container_width=True)

# BUSINESS INSIGHTS

st.markdown("---")

st.header(" Key Business Insights")

st.success("""
**Key findings from the analysis:**

-  Technology is the most profitable category.
-  Furniture generates high sales but relatively low profit.
-  Consumer customers contribute the largest share of sales.
-  November is the strongest sales month.
-  Discounts above 30% are frequently associated with losses.
""")

# FOOTER

st.markdown("---")

st.caption(
    "Developed by **Rethabile Mmako** | BSc Mathematical Sciences (Computer Science & Statistics)"
)