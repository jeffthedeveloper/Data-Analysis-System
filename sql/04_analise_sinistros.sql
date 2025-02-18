SELECT customer_id, insurance_type, COUNT(claims) AS total_claims
FROM insurance_claims
WHERE insurance_type = 'Automóvel'
GROUP BY customer_id, insurance_type;
