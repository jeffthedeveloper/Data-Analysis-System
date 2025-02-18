SELECT p.name, COUNT(*) AS times_bought
FROM products p
INNER JOIN purchase_history ph ON p.product_id = ph.product_id
GROUP BY p.name
ORDER BY times_bought DESC;
