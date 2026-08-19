CREATE DATABASE sales_db;
USE sales_db;
CREATE TABLE Customer(
    Customer_id INT PRIMARY KEY,
    Name VARCHAR(50),
    City VARCHAR(50),
    Age INT
);
INSERT INTO Customer VALUES
(1,'Diya','Ahemdabad',20),
(2, 'Aarav', 'Surat', 21),
(3, 'Riya', 'Vadodara', 19),
(4, 'Neha', 'Rajkot', 20),
(5, 'Krisha', 'Ahmedabad', 22);