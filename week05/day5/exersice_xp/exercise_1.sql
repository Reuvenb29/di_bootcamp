-- Drop tables if they exist (for re-runs)
DROP TABLE IF EXISTS customer_review;
DROP TABLE IF EXISTS new_film;
DROP TABLE IF EXISTS film;
DROP TABLE IF EXISTS language;

-- Step 1: Create a mock language table
CREATE TABLE language (
    language_id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

-- Insert sample languages
INSERT INTO language (name) VALUES 
('English'),
('French'),
('Spanish');

-- Step 2: Create a mock film table
CREATE TABLE film (
    film_id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    language_id INT REFERENCES language(language_id)
);

-- Insert sample films
INSERT INTO film (title, description, language_id) VALUES 
('The Matrix', 'A computer hacker learns about the true nature of reality.', 1),
('Amélie', 'A quirky girl helps others in small, magical ways.', 2);

-- Step 3: Get all languages
SELECT * FROM language;

-- Step 4: Films joined with languages (INNER JOIN)
SELECT 
    film.title, 
    film.description, 
    language.name AS language_name
FROM film
JOIN language ON film.language_id = language.language_id;

-- Step 5: All languages, even if there are no films (LEFT JOIN)
SELECT 
    film.title, 
    film.description, 
    language.name AS language_name
FROM language
LEFT JOIN film ON film.language_id = language.language_id;

-- Step 6: Create new_film table
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- Add new films
INSERT INTO new_film (name) VALUES 
('Blade Runner'),
('Spirited Away');

-- Step 7: Create customer_review table with cascading delete
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(100),
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Step 8: Add 2 reviews
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES
(1, 1, 'A dark sci-fi masterpiece', 9, 'Blade Runner is visually stunning and thought-provoking.'),
(2, 3, 'Enchanting and magical', 10, 'Spirited Away is a beautiful journey into fantasy.');

-- View customer reviews
SELECT * FROM customer_review;

-- Step 9: Delete a film and check cascading effect
DELETE FROM new_film WHERE id = 1;

-- Check reviews again
SELECT * FROM customer_review;
