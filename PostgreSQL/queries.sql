-- Example queries for PostgreSQL Showcase

-- Select all users
SELECT * FROM users;

-- Filter by condition
SELECT * FROM users WHERE name = 'Alice';

-- Count users
SELECT COUNT(*) FROM users;

-- Use CTE
WITH active_users AS (
  SELECT * FROM users WHERE email IS NOT NULL
)
SELECT * FROM active_users;

-- Example of window function
SELECT name, COUNT(*) OVER() AS total_users FROM users;
