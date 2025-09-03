-- PARTE 1

.open Chinook.db
.mode table

SELECT composer, unitprice, milliseconds 
FROM tracks;

.once 'parte1.txt'

SELECT name, composer, unitprice
FROM tracks;

-- PARTE 2

.output 'parte2.txt'

SELECT title
FROM albums
WHERE AlbumId = 67;

SELECT *
FROM artists
WHERE Name LIKE '%black%';

SELECT Name, Milliseconds
FROM tracks
WHERE Milliseconds BETWEEN 50000 AND 70000;

SELECT DISTINCT BillingCountry
FROM invoices;

SELECT FirstName || ' ' || LastName AS NomeCompleto, CustomerId, Country
FROM customers
WHERE Country = 'Brazil';

SELECT *
FROM employees
WHERE Title = 'Sales Agents';

SELECT DISTINCT BillingCity
FROM invoices
WHERE BillingCountry = 'Brazil' AND BillingCity <> 'São Paulo';

SELECT DISTINCT CustomerId
FROM invoices 
WHERE BillingCity = 'Brasília';

SELECT DISTINCT CustomerId
FROM customers
WHERE City = 'Brasília';

SELECT Name
FROM tracks
WHERE GenreId  = (SELECT GenreId FROM genres WHERE Name = 'Rock And Roll');

.output

-- PARTE 3

.output 'parte3.txt'

SELECT AlbumId
FROM albums 
WHERE Title = 'Dark Side Of The Moon';

SELECT Title AS 'Titulo Álbum', Name AS 'Artista'
FROM albums
JOIN artists
ON artists.ArtistId = albums.ArtistId
WHERE title LIKE '%black%' and Name LIKE '%black%';

SELECT Name AS 'Nome', Milliseconds as "Comprimento", Title as "Álbum"
FROM tracks
JOIN albums
ON albums.AlbumId = tracks.AlbumId
WHERE Milliseconds BETWEEN 50000 AND 70000;

SELECT FirstName || ' ' || LastName AS "Nome Completo", CustomerId, Country
FROM customers
WHERE FirstName LIKE 'A%';

SELECT DISTINCT FirstName, LastName
FROM customers
JOIN invoices
ON invoices.CustomerId = customers.CustomerId
WHERE BillingCountry = 'Brazil';


SELECT tracks.Name
FROM tracks
JOIN genres
ON tracks.GenreId = genres.GenreId
WHERE genres.Name = 'Rock And Roll';

.output