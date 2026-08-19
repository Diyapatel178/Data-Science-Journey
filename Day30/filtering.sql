SELECT * FROM Customer
WHERE City IN ('Ahmedabad','Surat','Rajkot');

SELECT * FROM Customer
WHERE Age BETWEEN 19 AND 21;

SELECT * FROM Customer 
WHERE City NOT IN ('Ahmedabad','Surat');

SELECT * FROM Customer
WHERE Age NOT BETWEEN 20 AND 22;