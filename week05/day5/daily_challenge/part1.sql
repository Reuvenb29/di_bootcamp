 PART I - One-to-One: Customer & Customer_Profile
-- ====================

-- Drop if exists (for clean reruns)
DROP TABLE IF EXISTS customer_profile CASCADE;
DROP TABLE IF EXISTS customer CASCADE;

-- 1. Create tables
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INT UNIQUE REFERENCES customer(id)
);

-- 2. Insert customers
INSERT INTO customer (first_name, last_name) VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

-- 3. Insert customer profiles using subqueries
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES 
(true, (SELECT id FROM customer WHERE first_name = 'John')),
(false, (SELECT id FROM customer WHERE first_name = 'Jerome'));

-- 4. JOINS and queries

-- A. First name of logged in customers
SELECT c.first_name
FROM customer c
JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = true;

-- B. All customers and their login status, including those without profiles
SELECT c.first_name, cp.isLoggedIn
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id;

-- C. Number of customers who are NOT logged in
SELECT COUNT(*) AS not_logged_in_count
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = false OR cp.isLoggedIn IS NULL;