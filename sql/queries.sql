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