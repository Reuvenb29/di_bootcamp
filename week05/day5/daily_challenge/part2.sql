PART II - Many-to-Many: Book, Student, Library
-- ====================

-- Drop existing tables
DROP TABLE IF EXISTS library CASCADE;
DROP TABLE IF EXISTS student CASCADE;
DROP TABLE IF EXISTS book CASCADE;

-- 1. Create book table
CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);

-- 2. Insert books
INSERT INTO book (title, author) VALUES
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

-- 3. Create student table with age constraint (age <= 15)
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
);

-- 4. Insert students
INSERT INTO student (name, age) VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

-- 5. Create junction table: Library
CREATE TABLE library (
    book_fk_id INT REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INT REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id)
);

-- 6. Insert borrow records using subqueries
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date) VALUES
((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
 (SELECT student_id FROM student WHERE name = 'John'),
 '2022-02-15'),

((SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
 (SELECT student_id FROM student WHERE name = 'Bob'),
 '2021-03-03'),

((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
 (SELECT student_id FROM student WHERE name = 'Lera'),
 '2021-05-23'),

((SELECT book_id FROM book WHERE title = 'Harry Potter'),
 (SELECT student_id FROM student WHERE name = 'Bob'),
 '2021-08-12');

-- 7. Queries

-- A. All columns from junction table
SELECT * FROM library;

-- B. Student name and book title
SELECT s.name AS student_name, b.title AS book_title
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id;

-- C. Average age of children who borrowed "Alice In Wonderland"
SELECT AVG(s.age) AS average_age
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

-- D. Delete a student and observe cascade
-- This will remove Bob and any borrow records by Bob in library
DELETE FROM student
WHERE name = 'Bob';

-- Check library table to confirm rows deleted
SELECT * FROM library;
