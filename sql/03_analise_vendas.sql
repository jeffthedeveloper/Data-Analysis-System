SELECT category, COUNT(*) AS total_sales, SUM(price) AS total_revenue
FROM products
GROUP BY category;
