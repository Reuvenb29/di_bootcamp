-- Create a minimal actors-style table
CREATE TABLE IF NOT EXISTS mini_actors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL
);

-- Insert two valid records
INSERT INTO mini_actors (name, birth_date)
VALUES
('Alice Smith', '1990-05-12'),
('Bob Johnson', '1985-03-30');

-- Count how many actors are in the table
SELECT COUNT(*) FROM mini_actors;

-- Try inserting blank/null fields (this should fail)
-- Expected error: null value in column "name" violates not-null constraint
INSERT INTO mini_actors (name, birth_date)
VALUES (NULL, NULL);
