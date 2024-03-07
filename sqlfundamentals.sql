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
SELECT 
    m.Title AS Movie_Title, 
    ROUND(((b.Domestic_sales + b.International_sales) / 1000000), 2) AS Combined_Sales_Millions
FROM 
    Movies m
JOIN 
    Boxoffice b ON m.Id = b.Movie_id;

SELECT title, rating * 10 AS rating_percent
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;

SELECT title, year
FROM movies
WHERE year % 2 = 0;

-- 10
SELECT max(Years_employed) as "longest time" FROM employees;

SELECT role, AVG(years_employed) as Average_years_employed
FROM employees
GROUP BY role;

SELECT building, SUM(years_employed) as Total_years_employed
FROM employees
GROUP BY building;

-- 11
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
SELECT director, count(director) as "movies directed"
FROM movies
GROUP BY director;

SELECT director, SUM(domestic_sales + international_sales) as Cumulative_sales_from_all_movies
FROM movies INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id
GROUP BY director;