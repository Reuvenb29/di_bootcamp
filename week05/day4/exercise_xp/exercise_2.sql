-- Select all columns from the customer table
SELECT * FROM customer;

-- Display full name using alias
SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- Get all unique create_date values
SELECT DISTINCT create_date FROM customer;

-- All customer details ordered by first name descending
SELECT * FROM customer ORDER BY first_name DESC;

-- Film details ordered by rental rate ascending
SELECT film_id, title, description, release_year, rental_rate 
FROM film 
ORDER BY rental_rate ASC;

-- Address and phone number for customers in Texas
SELECT address, phone 
FROM address 
WHERE district = 'Texas';

-- Movie details where ID is 15 or 150
SELECT * FROM film 
WHERE film_id IN (15, 150);

-- Check if my favorite movie exists
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title = 'The Matrix';

-- If spelling unsure, start with 'Th'
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title LIKE 'Th%';

-- 10 cheapest movies
SELECT * FROM film 
ORDER BY rental_rate ASC 
LIMIT 10;

-- Next 10 cheapest movies (bonus: using OFFSET)
SELECT * FROM film 
ORDER BY rental_rate ASC 
LIMIT 10 OFFSET 10;

-- Join customer and payment info
SELECT c.first_name, c.last_name, p.amount, p.payment_date 
FROM customer c 
JOIN payment p ON c.customer_id = p.customer_id 
ORDER BY c.customer_id;

-- Movies not in inventory
SELECT * FROM film 
WHERE film_id NOT IN (SELECT film_id FROM inventory);

-- Find cities with their countries
SELECT city.city, country.country 
FROM city 
JOIN country ON city.country_id = country.country_id;

-- Bonus: Seller performance by staff
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id 
FROM customer c 
JOIN payment p ON c.customer_id = p.customer_id 
ORDER BY p.staff_id;
