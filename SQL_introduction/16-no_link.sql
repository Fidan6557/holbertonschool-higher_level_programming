-- a script that lists all records of the table second_table of the database
-- a script that lists all records of the table second_table of the database
SELECT
SCORE AS 'score'
NAME AS 'name'
FROM second_table
WHERE NAME IS NOT NULL
ORDER BY SCORE DESC;