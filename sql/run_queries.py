import sqlite3
import pandas as pd

conn = sqlite3.connect("sql/retail_sales.db")

queries = {
    "Total Sales":
    """
    SELECT SUM(Sales) AS Total_Sales
    FROM sales;
    """,

    "Total Profit":
    """
    SELECT SUM(Profit) AS Total_Profit
    FROM sales;
    """,

    "Sales by Category":
    """
    SELECT Category,
           SUM(Sales) AS Total_Sales
    FROM sales
    GROUP BY Category
    ORDER BY Total_Sales DESC;
    """,

    "Profit by Category":
    """
    SELECT Category,
           SUM(Profit) AS Total_Profit
    FROM sales
    GROUP BY Category
    ORDER BY Total_Profit DESC;
    """,

    "Sales by Region":
    """
    SELECT Region,
           SUM(Sales) AS Total_Sales
    FROM sales
    GROUP BY Region
    ORDER BY Total_Sales DESC;
    """
}

for title, query in queries.items():
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    result = pd.read_sql_query(query, conn)
    pd.set_option("display.float_format", "{:,.2f}".format)
print(result)

conn.close()