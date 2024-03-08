-- 2. Where condition
SELECT * FROM movies 
where id = 6;

SELECT * FROM movies 
where year between 2000 and 2010;

SELECT * FROM movies 
where year not between 2000 and 2010;

SELECT title, year FROM movies 
where id <= 5;

-- 3. Queries with constraints pt.2
SELECT * FROM movies 
where title like "Toy Story%";

SELECT title FROM movies 
where director = "John Lasseter";

SELECT title, director FROM movies 
where director != "John Lasseter";

SELECT * FROM movies 
where title like "WALL-_";

-- in operator example
SELECT * FROM movies where year in (1999, 2007, 2012);
SELECT * FROM movies where year not in (1999, 2007, 2012);

-- 4. 
SELECT distinct director FROM movies order by director;

SELECT * FROM movies order by year desc limit 4;

SELECT * FROM movies order by title limit 5;

SELECT * FROM movies order by title limit 5 offset 5;

-- 5
SELECT city, population FROM north_american_cities where country like "canada";

SELECT * FROM north_american_cities where country like "united states" order by latitude desc;

SELECT * FROM north_american_cities WHERE Longitude < (SELECT Longitude FROM north_american_cities WHERE City = 'Chicago') ORDER BY Longitude;

SELECT * FROM north_american_cities where country like "mexico" order by population desc limit 2;

SELECT * FROM north_american_cities where country like "united%" order by population desc limit 2 offset 2;

-- 6 joins
SELECT * FROM movies
INNER JOIN Boxoffice  
    ON movies.id = Boxoffice.movie_id;

SELECT * FROM movies
INNER JOIN Boxoffice  
    ON movies.id = Boxoffice.movie_id
    Where international_sales>domestic_sales;

SELECT * FROM movies
INNER JOIN Boxoffice  
    ON movies.id = Boxoffice.movie_id
    order by rating desc;

-- 7
SELECT DISTINCT Building
FROM Employees;

SELECT Building_name, Capacity
FROM Buildings;

SELECT * FROM Buildings 
LEFT JOIN Employees ON Building_name = Building;

-- 8 is/ is not null
SELECT name, role 
FROM employees
WHERE building IS NULL;

SELECT building_name
FROM buildings 
left join employees 
on buildings.building_name = employees.building;

-- 9
SELECT m.Title, ROUND(((b.Domestic_sales + b.International_sales) / 1000000), 2) AS Combined_Sales_Millions
FROM Movies m JOIN Boxoffice b 
ON m.Id = b.Movie_id;

SELECT title, rating * 10 AS rating_percent
FROM movies INNER JOIN boxoffice 
ON movies.id = boxoffice.movie_id;

SELECT title, year
FROM movies
WHERE year % 2 = 0;

-- 10 group by uses each in statement
SELECT max(Years_employed) as max_years_employed FROM employees;

SELECT *, AVG(years_employed) as Average_years_employed FROM employees GROUP BY role;

SELECT *, SUM(years_employed) as Total_years_employed FROM employees GROUP BY building;

-- 11 having clause
SELECT role, count(role) AS Number
FROM employees
where role like "artist"
GROUP BY role

SELECT role, count(name)
FROM employees
GROUP BY role

SELECT role, sum(years_employed)
FROM employees
WHERE role like "engineer"
GROUP BY role

-- 12
SELECT director, count(director) AS movies_directed
FROM movies
GROUP BY director;

SELECT director, SUM(domestic_sales + international_sales) as total_sales
FROM movies INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id
GROUP BY director;

-- Order of sql statement as a whole:
-- SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
-- FROM mytable
--     JOIN another_table
--       ON mytable.column = another_table.column
--     WHERE constraint_expression
--     GROUP BY column
--     HAVING constraint_expression
--     ORDER BY column ASC/DESC
--     LIMIT count OFFSET COUNT;

-- 13 insert
-- Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)
INSERT INTO movies 
VALUES (4, "Toy Story 4", "El Directore", 2015, 90);

-- Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.
INSERT INTO boxoffice 
VALUES (4, 8.7, 340000000, 270000000);

-- 14 update
UPDATE movies 
SET director = "John Lasseter" 
WHERE id = 2;

UPDATE movies 
SET year = 1999 
WHERE id = 3;

SELECT * FROM movies WHERE id = 11;
UPDATE movies 
SET title = "Toy Story 3", director = "Lee Unkrich" 
WHERE id = 11;

-- 15 Deleting
SELECT * FROM movies WHERE year < 2005;
DELETE FROM movies WHERE year < 2005;

SELECT * FROM movies WHERE director = "Andrew Stanton";
DELETE FROM movies WHERE director = "Andrew Stanton";

-- 16 Creating a table
CREATE TABLE IF NOT EXISTS Database (
    Name TEXT, 
    Version FLOAT, 
    Download_count INTEGER
);

-- 17 Alter table 
ALTER TABLE movies
ADD Aspect_ratio FLOAT;

ALTER TABLE movies
ADD Language TEXT DEFAULT "English";

-- 18 Drop table
DROP TABLE IF EXISTS Movies;

DROP TABLE IF EXISTS BoxOffice;