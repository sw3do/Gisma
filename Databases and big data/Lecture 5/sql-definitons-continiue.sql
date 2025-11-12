CREATE SCHEMA GISMA_LECTURE_5;

use GISMA_LECTURE_5;

CREATE TABLE IF NOT EXISTS Suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    phone_number VARCHAR(20),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    country VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    stock INT DEFAULT 0,
    supplier_id INT NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    o_status VARCHAR(20) DEFAULT 'Pending',
    total_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE SET NULL /* Better Option */
);


CREATE TABLE IF NOT EXISTS Order_Details (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT DEFAULT 1,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    reference_code VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

INSERT INTO Suppliers (name, phone) VALUES
('Tech Supply Co', '+49-30-12345678'),
('Global Electronics', '+49-89-98765432'),
('Premium Parts GmbH', '+49-40-55512345'),
('Digital Wholesale', '+49-69-77788899'),
('Smart Components Ltd', '+49-221-33344455');

INSERT INTO Customers (first_name, last_name, email, phone_number, country) VALUES
('Max', 'Mustermann', 'max.mustermann@email.com', '+49-151-12345678', 'Germany'),
('Anna', 'Schmidt', 'anna.schmidt@email.com', '+49-170-98765432', 'Germany'),
('John', 'Smith', 'john.smith@email.com', '+44-20-12345678', 'UK'),
('Maria', 'Garcia', 'maria.garcia@email.com', '+34-91-98765432', 'Spain'),
('Pierre', 'Dubois', 'pierre.dubois@email.com', '+33-1-55512345', 'France'),
('Sarah', 'Johnson', 'sarah.johnson@email.com', '+1-555-0123', 'USA'),
('Hans', 'Mueller', 'hans.mueller@email.com', '+49-172-77788899', 'Germany'),
('Lisa', 'Weber', 'lisa.weber@email.com', '+49-176-33344455', 'Germany');

INSERT INTO Products (product_name, description, stock, supplier_id) VALUES
('Laptop Pro 15', 'High-performance laptop with 16GB RAM', 45, 1),
('Wireless Mouse', 'Ergonomic wireless mouse with USB receiver', 150, 2),
('Mechanical Keyboard', 'RGB mechanical gaming keyboard', 80, 1),
('USB-C Hub', '7-in-1 USB-C multiport adapter', 120, 3),
('External SSD 1TB', 'Portable solid state drive', 60, 4),
('Webcam HD', '1080p webcam with built-in microphone', 95, 2),
('Monitor 27 inch', '4K UHD IPS display', 35, 5),
('Headset Pro', 'Noise-cancelling wireless headset', 70, 3),
('Laptop Stand', 'Adjustable aluminum laptop stand', 110, 4),
('Cable Set', 'USB-C and HDMI cable bundle', 200, 5);

INSERT INTO Orders (customer_id, o_status, total_amount) VALUES
(1, 'Completed', 1299.99),
(2, 'Pending', 89.98),
(3, 'Shipped', 549.99),
(4, 'Completed', 199.97),
(1, 'Processing', 449.99),
(5, 'Completed', 899.99),
(6, 'Shipped', 159.98),
(7, 'Pending', 1849.98),
(8, 'Completed', 299.99),
(2, 'Processing', 679.98);

INSERT INTO Order_Details (order_id, product_id, quantity) VALUES
(1, 1, 1),
(2, 2, 2),
(2, 10, 1),
(3, 7, 1),
(4, 4, 1),
(4, 10, 2),
(5, 5, 1),
(6, 1, 1),
(7, 2, 1),
(7, 3, 1),
(8, 1, 1),
(8, 7, 1),
(9, 8, 1),
(10, 3, 2),
(10, 6, 1);

INSERT INTO Transactions (order_id, payment_method, reference_code, amount) VALUES
(1, 'Credit Card', 'TXN-CC-2024-001', 1299.99),
(3, 'PayPal', 'TXN-PP-2024-003', 549.99),
(4, 'Debit Card', 'TXN-DC-2024-004', 199.97),
(6, 'Credit Card', 'TXN-CC-2024-006', 899.99),
(9, 'Bank Transfer', 'TXN-BT-2024-009', 299.99);



SELECT SUM(total_amount) AS 'Total Sales', customer_id AS 'Customer ID' FROM Orders GROUP BY customer_id HAVING SUM(total_amount) > 1000;
-- LIKE WHERE BUT FOR AGGREGATES

SELECT SUM(total_amount) AS 'Total Sales', customer_id AS 'Customer ID' FROM Orders WHERE total_amount > 1000 GROUP BY customer_id;
-- THIS IS BETTER THAN HAVING AS IT FILTERS BEFORE AGGREGATION



SELECT country, COUNT(*) AS customer_count
FROM Customers
GROUP BY country
ORDER BY customer_count DESC;

SELECT 
    CASE 
        WHEN country = 'Germany' THEN 'Germany'
        WHEN country = 'UK' THEN 'United Kingdom'
        WHEN country = 'Spain' THEN 'Spain'
        WHEN country = 'France' THEN 'France'
        WHEN country = 'USA' THEN 'United States'
        ELSE 'Other Countries'
    END AS country_name,
    COUNT(*) AS customer_count
FROM Customers
GROUP BY country_name
ORDER BY customer_count DESC;


SELECT * 
FROM Customers
ORDER BY FIRST_NAME, LAST_NAME;

SELECT customer_id, o_status, COUNT(*)
FROM Orders
GROUP BY customer_id, o_status

ORDER BY customer_id, o_status;


-- SQL, A JOIN OPERATION COMBINES ROWS FROM TWO OR MORE TABLES BASED ON A RELATED COLUMN BETWEEN THEM. We have diffrent types of Join including INNER JOIN, RIGHT JOIN, FULL JOIN, LEFT JOIN

SELECT * FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Customers.country = 'Germany';

SELECT Orders.ORDER_ID, CONCAT(Customers.first_name, ' ', Customers.last_name) AS customer_name FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Customers.country = 'Germany';

-- First one is left table, second one is right table
-- oRDERS İS LEFT, Customers IS RIGHT


SELECT Orders.ORDER_ID, CONCAT(Customers.first_name, ' ', Customers.last_name) AS customer_name FROM Orders
INNER JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Customers.country = 'Germany';


SELECT Orders.ORDER_ID, CONCAT(Customers.first_name, ' ', Customers.last_name) AS customer_name FROM Orders
RIGHT JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Customers.country = 'Germany';

-- RIGHT JOIN AND INNER JOIN ARE SAME


SELECT Orders.ORDER_ID, CONCAT(Customers.first_name, ' ', Customers.last_name) AS customer_name FROM Orders
INNER JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Customers.country = 'Germany';


SELECT Orders.ORDER_ID, CONCAT(Customers.first_name, ' ', Customers.last_name) AS customer_name FROM Orders
LEFT JOIN Customers ON Orders.customer_id = Customers.customer_id;


SELECT Orders.ORDER_ID, CONCAT(Customers.first_name, ' ', Customers.last_name) AS customer_name FROM Orders
LEFT JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Orders.ORDER_ID IS NOT NULL;


SELECT P.PRODUCT_ID, P.PRODUCT_NAME, S.NAME AS SUPPLIER_NAME
FROM PRODUCTS P
JOIN SUPPLIERS S ON P.SUPPLIER_ID = S.SUPPLIER_ID;


SELECT OD.ORDER_ID, P.PRODUCT_NAME, P.PRODUCT_ID, O.ORDER_DATE
FROM ORDER_DETAILS OD
JOIN PRODUCTS P ON OD.PRODUCT_ID = P.PRODUCT_ID
JOIN ORDERS O ON OD.ORDER_ID = O.ORDER_ID
---------

-- Set Theory

-- Set theory operators allow you to peform operations similar to those in mathematical set theory. tHESE oPERATORS Enable you to manipulate and combine the result of multiple SQL queries.

-- UNION
-- INTERSECT
-- EXCEPT
-- UNION ALL

SELECT Customer_ID from Customers
UNION
Select Customer_ID from Orders;

SELECT Customer_ID from Customers
UNION ALL
Select Customer_ID from Orders;

SELECT * FROM Orders O
RIGHT JOIN Customers C ON O.Customer_ID = C.Customer_ID
UNION ALL
SELECT * FROM Orders O
RIGHT JOIN Customers C ON O.Customer_ID = C.Customer_ID

SELECT Customer_ID from Customers
UNION ALL
Select Customer_ID from Orders;

---


SELECT Customer_ID from Customers
EXCEPT
Select Customer_ID from Orders;

---


SELECT Customer_ID from Customers
INTERSECT
Select Customer_ID from Orders;