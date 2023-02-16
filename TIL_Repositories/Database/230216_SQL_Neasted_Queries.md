# SQL - Neasted_Queries

## 학습 목표

> SQL subquery가 무엇인지 이해하고, 조건에 따라 하나 이상의 테이블에서 데이터를 검색할 수 있다.

> SELECT, FROM, WHERE 절 등 다양한 맥락에서 사용하는 subquery를 작성할 수 있다.

# 1. Introduction to Subquery
- Subquery: A query inside a query
- 단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법

### Subquery 예시
- table1 에서 가장 나이가 어린 사람을 삭제해야 한다면?

``` SQL
DELETE FROM table1
WHERE age = ( -- 여기서부터 Subquery
	SELECT MIN(age) FROM table1
);
```
### Subquery 특징
- 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는 데 사용
-SELECT, FROM, WHERE, HAVING 절 등에서 다양한 맥락에서 사용

### Subquery practice #1
- 가장 많은 돈을 소비한 고객 번호 조회(payments 테이블 활용)

``` SQL
SELECT customerNumber, amount
FROM payments
WHERE amount = (
	SELECT MAX(amount) 
    FROM payments
);
```

### Subquery practice #2
- 미국에 있는 사무실에서 근무하는 직원의 이름과 성 조회(직원 정보는 employees, 사무실 정보는 offices 테이블에 존재)

``` SQL
SELECT lastName, firstName
FROM employees
WHERE officecode in (
	SELECT officeCode 
	FROM offices
	WHERE country = 'USA'
    );
```

### Subquery practice #3
- 주문한 적이 없는 고객 목록 조회(고객 정보는 customers, 주문 정보는 orders 테이블에 존재)

``` SQL
SELECT customerName
FROM customers
WHERE customerNumber NOT IN (
	SELECT DISTINCT customerNumber 
	FROM orders
    );
```
### Subquery practice #1 - 심화
- 소비를 한 고객들 중 지불한 금액의 가장 높은 고객의 customerNumber, amount, contactFirstName을 조회(고객 테이블은 customers, 지불 테이블은 payments를 활용)

``` SQL
SELECT customerNumber, amount, contactFirstName
FROM ( -- subqurey로 INNER JOIN 사용
	SELECT *
    FROM payments
    INNER JOIN customers USING (customerNumber)
) AS mySub -- FROM 절에서 사용하는 subqurey에 대해서 이름 지정해야 함
WHERE amount = (
	SELECT MAX(amount)
    FROM payments
);
```

## `EXISTS` operator
- 쿼리 문에서 반환된 레코드의 존재 여부를 확인

### EXISTS syntax

``` SQL
SELECT 
    select_list
FROM
    table
WHERE
    [NOT] EXISTS (subquery);
```

- subquery가 하나 이상의 행을 반환하면 EXISTS 연산자는 true를 반환하고 그렇지 않으면 false를 반환
- 주로 WHERE 절에서 subquery의 반환 값 존재 여부를 확인하는데 사용


### EXISTS practice #1
- 적어도 한번 이상 주문을 한 고객들의 번호와 이름 조회(고객 테이블은 customers, 주문 테이블은 orders이며 두 테이블의 customerNumber 필드를 기준으로 비교)

``` SQL
SELECT customerNumber, customerName
FROM customers
WHERE
	EXISTS(
		SELECT *
		FROM orders
        WHERE customers.customerNumber = orders.customerNumber
);
```

### EXISTS practice #2
- Paris에 있는 사무실에서 일하는 모든 직원의 번호, 이름, 성을 조회(직원 테이블은 employees, 사무실 테이블은 offices이며 두 테이블의 officeCode 필드를 기준으로 비교)


# 2. Conditional Statements

## `CASE` statement
- SQL 문에서 조건문을 구성

## CASE syntax

``` SQL
CASE case_value
    WHEN when_value1 THEN statements
    WHEN when_value2 THEN statements
    ...
    [ELSE else-statements]
END CASE;
```

- case_value가 when_value와 동일한 것을 찾을 때까지 순차적으로 비교
- when_value와 동일한 case_value를 찾으면 해당 THEN 절의 코드를 실행
- 동일한 값을 찾지 못하면 ELSE 절의 코드를 실행
    - ELSE 절이 없을 때 동일한 값을 찾지 못하면 오류 발생


### CASE practice #1
- 고객들의 creditLimit에 따라 VIP, Platinum, Bronze 등급을 매겨 조회(VIP는 100000 초과, Platinum은 70000 초과 그 외는 Bronze로 지정)

``` SQL
SELECT contactFirstName, creditLimit,
	CASE
		WHEN creditLimit > 100000 THEN 'VIP'
		WHEN creditLimit > 70000 THEN 'Platinum'
		ELSE 'Bronze'
	END AS grade
FROM customers;
```


### CASE practice #2
- orders 테이블의 status에 따라 상세 정보를 매겨 조회('In Progrss'는 '주문 중', 'Shipped'는 '발주완료', 'Cancelled'는 '주문취소' 그 외는 '기타사유'로 지정)

``` SQL
SELECT orderNumber, status,
	CASE
		WHEN status = 'In Progrss' THEN '주문 중'
		WHEN status = 'Shipped' THEN '발주완료'
		WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
	END AS details
FROM orders;
```