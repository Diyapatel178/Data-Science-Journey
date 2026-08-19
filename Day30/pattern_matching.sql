SELECT * FROM Customer
WHERE Name LIKE 'D%';

SELECT * FROM Customer
WHERE Name LIKE '%a';

SELECT * FROM Customer
WHERE Name LIKE '%iy%';

SELECT * FROM Customer
WHERE Name LIKE '_iya';

SELECT * FROM Customer
WHERE Name LIKE 'D%'
AND Age > 18;

SELECT * FROM Customer
WHERE Name LIKE '_____';