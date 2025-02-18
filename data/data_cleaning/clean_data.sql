-- Limpeza de dados duplicados
DELETE FROM customers
WHERE customer_id IN (SELECT customer_id FROM customers GROUP BY customer_id HAVING COUNT(*) > 1);
