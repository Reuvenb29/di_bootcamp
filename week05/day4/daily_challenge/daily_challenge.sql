-- Create FirstTab
CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

-- Insert values
INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

-- View FirstTab
SELECT * FROM FirstTab;

-- Create SecondTab
CREATE TABLE SecondTab (
    id integer
);

-- Insert values
INSERT INTO SecondTab VALUES
(5),
(NULL);

-- View SecondTab
SELECT * FROM SecondTab;


-- Q1: Expected Output = 0
SELECT COUNT(*) AS Q1_Result
FROM FirstTab AS ft 
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id IS NULL
);


-- Q2: Expected Output = 3
SELECT COUNT(*) AS Q2_Result
FROM FirstTab AS ft 
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id = 5
);


-- Q3: Expected Output = 0
SELECT COUNT(*) AS Q3_Result
FROM FirstTab AS ft 
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab
);


-- Q4: Expected Output = 3
SELECT COUNT(*) AS Q4_Result
FROM FirstTab AS ft 
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id IS NOT NULL
);
