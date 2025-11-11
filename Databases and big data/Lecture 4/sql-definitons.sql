USE ecommerce_gisma_world;

-- DQL

CREATE TABLE Suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(50)
);

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    phone_number VARCHAR(20),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    country VARCHAR(50)
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    stock INT DEFAULT 0,
    supplier_id INT NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    o_status VARCHAR(20) DEFAULT 'Pending',
    total_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE SET NULL /* Better Option */
);

CREATE TABLE Order_Details (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT DEFAULT 1,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    reference_code VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);



-- DML

INSERT INTO Suppliers (name, phone)
VALUES ('Tech Supplies Co.', '555-1234');

INSERT INTO Customers (first_name, last_name, email, phone_number, country)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', 'USA'), 
       ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 'Canada');

INSERT INTO Products (product_name, description, stock, supplier_id)
VALUES ('Laptop', 'High-performance laptop', 10, 1);

INSERT INTO Orders (customer_id, total_amount)
VALUES (1, 1500.00);

INSERT INTO Order_Details (order_id, product_id, quantity)
VALUES (1, 1, 1);

INSERT INTO Transactions (order_id, payment_method, reference_code, amount)
VALUES (1, 'Credit Card', 'REF123456', 1500.00);

-- DQL Again

SELECT * FROM Customers;
SELECT * FROM Orders WHERE o_status = 'Pending';

SELECT order_id, customer_id, total_amount FROM Orders;

    SELECT * FROM Customers WHERE country = 'USA';


    SELECT * FROM Customers WHERE first_name LIKE 'J%';
    SELECT * FROM Customers WHERE first_name LIKE 'J_n%';


SELECT * FROM Customers WHERE country IS NULL;
SELECT * FROM Customers WHERE country IS NOT NULL;

    SELECT * FROM Customers  WHERE country IN ('USA', 'Canada', 'UK');

    SELECT * FROM Customers  WHERE country = 'USA' OR countery = 'Canada' OR countery = 'UK';

    SELECT * FROM Orders WHERE total_amount > 100 and total_amount < 1000;

     SELECT * FROM Orders WHERE total_amount BETWEEN 100 AND 1000;


/* 

= // EQUAL
!= // NOT EQUAL
<> // NOT EQUAL
> // GREATER THAN
< // LESS THAN
>= // GREATER THAN OR EQUAL TO
<= // LESS THAN OR EQUAL TO

*/


-- DML

UPDATE Customers 
SET country = 'Unknown'
WHERE country IS NULL;

SELECT * FROM Customers WHERE country = 'Unknown';
DELETE FROM Customers WHERE country = 'Unknown' OR customer_id = 1;


-- DQL

SELECT * FROM Customers ORDER by first_name;
SELECT * FROM Customers ORDER by first_name ASC;
SELECT * FROM Customers ORDER by country DESC;

SELECT * FROM Customers WHERE country IS NOT NULL ORDER by country ASC, first_name DESC;

SELECT DISTINCT country FROM Customers;


SELECT DISTINCT country AS 'Country Name' FROM Customers;

SELECT country AS 'Country Name', first_name AS 'First Name', last_name AS 'Last Name', email AS 'Email' FROM Customers;


SELECT COUNT(*) AS 'Total Customers', country AS 'Country' FROM Customers GROUP BY country;


SELECT SUM(total_amount) AS 'Total Sales', customer_id AS 'Customer ID' FROM Orders GROUP BY customer_id;

SELECT AVG(total_amount) AS 'Average Sales', customer_id AS 'Customer ID' FROM Orders GROUP BY customer_id;

SELECT MIN(total_amount) AS 'Minimum Sales', customer_id AS 'Customer ID' FROM Orders GROUP BY customer_id;

SELECT MAX(total_amount) AS 'Maximum Sales', customer_id AS 'Customer ID' FROM Orders GROUP BY customer_id;

SELECT * FROM Customers WHERE first_name LIKE '____';
SELECT * FROM Customers WHERE first_name LIKE '____%';

SELECT * FROM Customers WHERE LENGTH(first_name) = 4;
SELECT * FROM Customers WHERE LENGTH(first_name) >= 4;
SELECT * FROM Customers WHERE LENGTH(first_name) BETWEEN 4 AND 6;

SELECT UPPER(first_name) FROM Customers WHERE LENGTH(first_name) BETWEEN 4 AND 6;
SELECT LOWER(first_name) FROM Customers WHERE LENGTH(first_name) BETWEEN 4 AND 6;

SELECT UPPER(first_name) AS 'First Name Uppercase', LOWER(last_name) AS 'Last Name Lowercase', CONCAT(first_name, ' ', last_name) AS 'Full Name' FROM Customers WHERE LENGTH(first_name) BETWEEN 4 AND 6;


SELECT NOW(), CURDATE() AS 'Current Date', CURTIME() AS 'Current Time', DATE(NOW()) AS 'Date from NOW()', YEAR(NOW()) AS 'Year from NOW()', MONTH(NOW()) AS 'Month from NOW()', DAY(NOW()) AS 'Day from NOW()';


SELECT ORDER_ID, ORDER_DATE,
CASE
           WHEN total_amount = < 100 THEN 'Low'
           WHEN total_amount BETWEEN 100 AND 500 THEN 'Medium'
           WHEN total_amount > 500 THEN 'High'
           END AS 'Order Value'
FROM Orders

SELECT customer_id, o_status, COUNT(*)
FROM Orders
GROUP BY customer_id, o_status