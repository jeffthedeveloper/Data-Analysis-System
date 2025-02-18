SELECT customer_id, name, age, location
FROM customers
WHERE location = 'São Paulo'
AND contract_expiration_date > NOW();
