DELETE FROM table1
WHERE age = (
	SELECT MIN(age) FROM table1
);


-- Subquery practice #1
-- - 가장 많은 돈을 소비한 고객 번호 조회(payments 테이블 활용)

SELECT customerNumber, amount
FROM payments
WHERE amount = (
	SELECT MAX(amount) 
    FROM payments
);

SELECT * FROM employees;
SELECT * FROM offices;

-- Subquery practice #2
-- 미국에 있는 사무실에서 근무하는 직원의 이름과 성 조회(직원 정보는 employees, 사무실 정보는 offices 테이블에 존재)

SELECT lastName, firstName
FROM employees
WHERE officecode in (
	SELECT officeCode 
	FROM offices
	WHERE country = 'USA'
    );
    
-- Subquery practice #3
-- 주문한 적이 없는 고객 목록 조회(고객 정보는 customers, 주문 정보는 orders 테이블에 존재)

SELECT * FROM customers;
SELECT * FROM orders;

SELECT customerName
FROM customers
WHERE customerNumber NOT IN (
	SELECT DISTINCT customerNumber 
	FROM orders
    );
    
    
-- Subquery practice #1 - 심화
-- 소비를 한 고객들 중 지불한 금액의 가장 높은 고객의 customerNumber, amount, contactFirstName을 조회
-- (고객 테이블은 customers, 지불 테이블은 payments를 활용)

SELECT * FROM customers;

SELECT customerNumber, amount, contactFirstName
FROM (
	SELECT *
    FROM payments
    INNER JOIN customers USING (customerNumber)
) AS mySub -- subQurey에 대해서 이름 지정
WHERE amount = (
	SELECT MAX(amount)
    FROM payments
);



-- EXISTS practice #1
-- 적어도 한번 이상 주문을 한 고객들의 번호와 이름 조회
-- (고객 테이블은 customers, 주문 테이블은 orders이며 두 테이블의 customerNumber 필드를 기준으로 비교)

SELECT customerNumber, customerName
FROM customers
WHERE
	EXISTS(
		SELECT *
		FROM orders
        WHERE customers.customerNumber = orders.customerNumber
);


-- EXISTS practice #2
-- Paris에 있는 사무실에서 일하는 모든 직원의 번호, 이름, 성을 조회(직원 테이블은 employees, 
-- 사무실 테이블은 offices이며 두 테이블의 officeCode 필드를 기준으로 비교)

SELECT * FROM employees;
SELECT * FROM offices;

SELECT employeeNumber, firstName, lastName
FROM employees
WHERE EXISTS (
	SELECT * 
	FROM offices
	WHERE city = 'Paris' AND employees.officeCode = offices.officeCode
);


-- CASE practice #1
-- 고객들의 creditLimit에 따라 VIP, Platinum, Bronze 등급을 매겨 조회
-- (VIP는 100000 초과, Platinum은 70000 초과 그 외는 Bronze로 지정)

SELECT contactFirstName, creditLimit,
	CASE
		WHEN creditLimit > 100000 THEN 'VIP'
		WHEN creditLimit > 70000 THEN 'Platinum'
		ELSE 'Bronze'
	END AS grade
FROM customers;


-- CASE practice #2
-- orders 테이블의 status에 따라 상세 정보를 매겨 조회
-- ('In Progrss'는 '주문 중', 'Shipped'는 '발주완료', 'Cancelled'는 '주문취소' 그 외는 '기타사유'로 지정)

SELECT orderNumber, status,
	CASE
		WHEN status = 'In Progrss' THEN '주문 중'
		WHEN status = 'Shipped' THEN '발주완료'
		WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
	END AS details
FROM orders;