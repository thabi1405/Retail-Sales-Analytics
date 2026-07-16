-- 1. Total Sales

SELECT
SUM(Sales) AS Total_Sales
FROM sales;


-- 2. Total Profit

SELECT
SUM(Profit) AS Total_Profit
FROM sales;


-- 3. Sales by Category

SELECT
Category,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;


-- 4. Profit by Category

SELECT
Category,
SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 5. Sales by Region

SELECT
Region,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- Top 5 Customers by Profit
SELECT
    [Customer Name],
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY [Customer Name]
ORDER BY Total_Profit DESC
LIMIT 5;

-- Average Profit by Category
SELECT
    Category,
    ROUND(AVG(Profit), 2) AS Average_Profit
FROM sales
GROUP BY Category
ORDER BY Average_Profit DESC;

-- Total Orders by Region
SELECT
    Region,
    COUNT(*) AS Total_Orders
FROM sales
GROUP BY Region
ORDER BY Total_Orders DESC;

-- Top 10 States by Sales
SELECT
    [State/Province],
    SUM(Sales) AS Total_Sales
FROM sales
GROUP BY [State/Province]
ORDER BY Total_Sales DESC
LIMIT 10;

-- Average Shipping Days
SELECT
    ROUND(AVG([Shipping Days]),2) AS Average_Shipping_Days
FROM sales;

-- Top 3 Products by Profit
SELECT
    [Product Name],
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY [Product Name]
ORDER BY Total_Profit DESC
LIMIT 3;