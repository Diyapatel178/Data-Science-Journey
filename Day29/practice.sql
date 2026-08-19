SELECT Name,Age FROM Customer
WHERE Age = 20;

SELECT Name,City FROM Customer
WHERE City = 'Ahmedabad';

SELECT * FROM Customer
WHERE Age = 20
AND City = 'Ahmedabad';

SELECT Name,Age FROM Customer
WHERE Age < 20
OR City = 'Rajkot';

SELECT *FROM Customer
WHERE Age >= 20
AND City = 'Ahmedabad'
OR City = 'Surat';

SELECT NAME,City,Age FROM Customer
WHERE Age > 20
OR City = 'Rajkot';