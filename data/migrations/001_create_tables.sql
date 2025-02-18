-- Criação das tabelas no banco de dados
CREATE TABLE customers (
    customer_id BIGINT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    location VARCHAR(100),
    contract_expiration_date DATE
);
