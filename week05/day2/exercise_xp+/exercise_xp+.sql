-- Create database
CREATE DATABASE bootcamp;

-- You’ll need to manually connect to the database in psql:
-- \c bootcamp

-- Create students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE
);

-- Insert student data
INSERT INTO students (first_name, last_name, birth_date) VALUES
('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-10-03'),
('Reuven', 'YourLastName', '199X-XX-XX');  -- Replace with your own birth date

-- Queries

-- 1. All students
SELECT * FROM students;

-- 2. All first and last names
SELECT first_name, last_name FROM students;

-- 3. Student with id = 2
SELECT first_name, last_name FROM students WHERE id = 2;

-- 4. Student named Marc Benichou
SELECT first_name, last_name FROM students WHERE first_name = 'Marc' AND last_name = 'Benichou';

-- 5. Students with last name Benichou OR first name Marc
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- 6. First names that contain "a"
SELECT first_name, last_name FROM students WHERE first_name ILIKE '%a%';

-- 7. First names that start with "a"
SELECT first_name, last_name FROM students WHERE first_name ILIKE 'a%';

-- 8. First names that end with "a"
SELECT first_name, last_name FROM students WHERE first_name ILIKE '%a';

-- 9. Second-to-last letter is "a"
SELECT first_name, last_name FROM students WHERE first_name ILIKE '%a_';

-- 10. Students with id 1 or 3
SELECT first_name, last_name FROM students WHERE id IN (1, 3);

-- 11. Students born on or after 2000-01-01
SELECT * FROM students WHERE birth_date >= '2000-01-01';
