SELECT * FROM users;
SELECT * FROM articles;

 TABLE users ( 
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
	title VARCHAR(50) NOT NULL,
	content VARCHAR(100) NOT NULL,
	userId INT NOT NULL,
	PRIMARY KEY (id)
);

INSERT INTO
	users (name)
VALUES
	('권미자'),
    ('류준하'),
    ('정영식');

INSERT INTO
	articles (title, content, userId)
VALUES
	('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 4);

SELECT title, content, name
FROM articles
INNER JOIN users
    ON articles.userId = users.id;
    
-- INNER JOIN practice #1
-- 제시된 두 테이블을 참고하여 productLine 값이 같은 레코드의 
-- productCode, productName 필드를 조회

SELECT productCode, productName, textDescription
FROM products
INNER JOIN productlines
    ON products.productline = productlines.productline;


-- INNER JOIN practice #2
-- 제시된 두 테이블을 참고하여 orderNumber 값이 같은 레코드의 
-- orders 테이블 orderNumber, status 필드를 조회

SELECT orders.orderNumber, status, priceEach, 
	quantityOrdered * priceEach AS take
FROM orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;
	


-- INNER JOIN practice #3
-- 직전 조회 결과를 바탕으로 각 주문번호 별 주문상태와 총 판매액을 요약
-- (주문번호는 orderNumber필드, 총 판매액은 quantityOrdered와 
-- priceEach필드의 곱셈 결과)

SELECT orders.orderNumber, status, 
	SUM(quantityOrdered * priceEach) AS totalSales
FROM orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber
GROUP BY orderNumber;


-- LEFT JOIN practice #1
-- 제시된 두 테이블을 참고하여 customers를 기준으로 customerNumber 
-- 필드가 일치하는 레코드와 함께 customers 테이블 contactFirstName와 
-- orders 테이블의 orderNumber, status 필드 조회 
-- (왼쪽 테이블은 customers, 오른쪽 테이블은 orders, 
-- 일치하지 않는 경우 NULL)

SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber;


-- LEFT JOIN practice #2
-- 직전 조회 결과를 바탕으로 주문 내역이 없는 고객의 이름과 주문번호 및 
-- 배송상태 조회 (고객의 이름은 contactFirstName필드, 
-- 주문번호는 orderNumber, 배송상태는 status 필드)


SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE orderNumber is NULL;


-- RIGHT JOIN practice #1
-- 제시된 두 테이블을 참고하여 employees를 기준으로 employeeNumber 필드와 
-- salesRepEmployeeNumber 필드가 일치하는 레코드와 함께 
-- employeeNumber, firstName, customerNumber, 
-- contactFirstName 필드 조회
-- (왼쪽 테이블은 customers, 오른쪽 테이블은 employees, 
-- 일치하지 않는 경우 NULL)

SELECT employeeNumber, firstName, customerNumber, contactFirstName
FROM customers
RIGHT JOIN employees
	ON employees.employeeNumber = customers.salesRepEmployeeNumber;


-- RIGHT JOIN practice #2
-- 직전 조회 결과를 바탕으로 고객에게 판매한 내역이 없는 직원 목록 조회 
-- (직원 번호와 이름은 employeeNumber, contactFirstName 필드이며 
-- 고객의 번호와 이름은 customerNumber, contactFirstName 필드)


SELECT employeeNumber, firstName, customerNumber, contactFirstName
FROM customers
RIGHT JOIN employees
	ON salesRepEmployeeNumber = employeeNumber
WHERE salesRepEmployeeNumber IS NULL;