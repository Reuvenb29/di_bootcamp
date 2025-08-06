-- Create the items table
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price INTEGER
);

-- Create the customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);

-- Insert items
INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

-- Insert customers
INSERT INTO customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

-- Queries
SELECT * FROM items;
SELECT * FROM items WHERE price > 80;
SELECT * FROM items WHERE price <= 300;
SELECT * FROM customers WHERE last_name = 'Smith';
SELECT * FROM customers WHERE last_name = 'Jones';
SELECT * FROM customers WHERE first_name != 'Scott';
