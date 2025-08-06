-- 🌟 Exercise 1: Items and Customers
-- This script creates sample tables and executes all required queries
-- Author: Reuven
-- Date: Week 5 Daily Challenge

-- Drop tables if they already exist (for re-runs)
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS customers;

-- Create the items table
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price INTEGER
);

-- Create the customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- Insert sample data into items table
INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80),
('Chair', 150),
('Lamp', 90);

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

-- ✅ Query 1: All items, ordered by price (lowest to highest)
SELECT * FROM items
ORDER BY price ASC;

-- ✅ Query 2: Items with a price >= 80, ordered by price (highest to lowest)
SELECT * FROM items
WHERE price >= 80
ORDER BY price DESC;

-- ✅ Query 3: First 3 customers in alphabetical order of first name (A-Z), excluding ID
SELECT first_name, last_name FROM customers
ORDER BY first_name ASC
LIMIT 3;

-- ✅ Query 4: All last names only, in reverse alphabetical order (Z-A)
SELECT last_name FROM customers
ORDER BY last_name DESC;
