SELECT * FROM Customer
WHERE City IN ('Ahmedabad','Surat','Rajkot');

SELECT * FROM Customer
WHERE Age BETWEEN 20 AND 25;

SELECT * FROM Customer
ORDER BY Age ASC;

SELECT * FROM Customer
WHERE Name LIKE 'D%';

SELECT * FROM Customer
WHERE Age BETWEEN 20 AND 25
AND Name LIKE 'A%'
ORDER BY Age DESC;

SELECT * FROM Customer
WHERE City IN ('Ahmedabad','Surat')
AND Age BETWEEN 20 AND 23
AND Name LIKE '%a%'
ORDER BY Age DESC;