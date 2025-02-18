CREATE TABLE customers (
    customer_id BIGINT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    location VARCHAR(100),
    contract_expiration_date DATE
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);
