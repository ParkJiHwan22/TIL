# SQL - Multi_Table_Queries

## 학습 목표

> 관계형 데이터베이스에서 외래 키 필드의 역할을 설명할 수 있다.

> MySQL JOIN 키워드의 유형 각 3가지의 특징을 설명할 수 있다.

> 주어진 예시에 맞추어 적절한 JOIN 키워드 유형을 작성해 정확한 결과를 반환할 수 있다.

# 1. Introduction to join
- 관계형 데이터베이스: 데이터 간에 `관계`가 있는 데이터 항목들의 모음
- 관계: `여러` 테이블 간의 (논리적) 연결

### 커뮤니티 게시판 예시
- 자유 게시판에 필요한 데이터 생각해보기
    - 제목, 내용, 작성자, 정보 등

``` SQL
SELECT * FROM 테이블 WHERE writer = '권미자';
```

- 생기는 문제점
    1. 동명이인일 수 있음
    2. 특정 데이터가 수정될 수 있음
    3. `데이터 관리`가 너무 어려움

- 테이블을 분리하면 관리는 용이해질 수 있으나 출력할 때는 테이블 한 개씩만 출력할 수 있기 때문에 `다른 테이블과 연결지어 출력`하는 것이 필요

# 2. Joining tables

## `Join` clause
- 둘 이상의 테이블에서 데이터를 검색하는 법

## JOIN 종류
- INNER JOIN
- OUTER JOIN
    - LEFT JOIN
    - RIGHT JOIN
- CROSS JOIN

## `INNER JOIN` clause
- 두 테이블에서 일치하는 레코드에 대해서만 결과를 반환

### INNER JOIN syntax

``` SQL
SELECT
    select_list
FROM
    table1
INNER JOIN table2
    ON table1.fk = table2.pk;
```

- FROM 절 이후 메인 테이블 지정 (table1)
- INNER JOIN 절 이후 메인 테이블과 조인할 테비을을 지정(table2)
- ON 키워드 이후 조인 조건을 작성
    - 조인 조건은 table1과 table2 간의 레코드를 일치시키는 규칙을 지정

``` SQL
SELECT title, content, name
FROM articles
INNER JOIN users
    ON articles.userId = users.id;
```

### INNER JOIN practice #1
- 제시된 두 테이블을 참고하여 productLine 값이 같은 레코드의 productCode, productName 필드를 조회

``` SQL
SELECT productCode, productName, textDescription
FROM products
INNER JOIN productlines
    ON products.productline = productlines.productline;
```


### INNER JOIN practice #2
- 제시된 두 테이블을 참고하여 orderNumber 값이 같은 레코드의 orders 테이블 orderNumber, status 필드를 조회

``` SQL
SELECT orders.orderNumber, status, priceEach, 
	quantityOrdered * priceEach AS take
FROM orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;
```


### INNER JOIN practice #3
- 직전 조회 결과를 바탕으로 각 주문번호 별 주문상태와 총 판매액을 요약(주문번호는 orderNumber필드, 총 판매액은 quantityOrdered와 priceEach필드의 곱셈 결과)

``` SQL
SELECT orders.orderNumber, status, 
	SUM(quantityOrdered * priceEach) AS totalSales -- SUM 사용해야함
FROM orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber
GROUP BY orderNumber; -- GROUP BY 의 위치
```


## `LEFT JOIN` clause
- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드를 반환

### LEFT JOIN syntax

``` SQL
SELECT
    select_list
FROM
    table1
LEFT [OUTER] JOIN table2
    ON table1.fk = table2.pk;
```

- FROM 절 이후 왼쪽 테이블 지정 (table1)
- LEFT JOIN 절 이후 오른쪽 테이블 지정 (table2)
- ON 키워드 이후 조인 조건을 작성
    - 왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴

### LEFT JOIN 특징
- 왼쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시
- 왼쪽 테이블 한 개의 레코드에 여러 개의 오른쪽 테이블 레코드가 일치할 경우, 해당 왼쪽 레코드를 여러 번 표시

### LEFT JOIN practice #1
- 제시된 두 테이블을 참고하여 customers를 기준으로 customerNumber 필드가 일치하는 레코드와 함께 customers 테이블 contactFirstName와 orders 테이블의 orderNumber, status 필드 조회 (왼쪽 테이블은 customers, 오른쪽 테이블은 orders, 일치하지 않는 경우 NULL)

``` SQL
SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber;
```

### LEFT JOIN practice #2
- 직전 조회 결과를 바탕으로 주문 내역이 없는 고객의 이름과 주문번호 및 배송상태 조회 (고객의 이름은 contactFirstName필드, 주문번호는 orderNumber, 배송상태는 status 필드)

``` SQL
SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE orderNumber is NULL;
```

## `RIGHT JOIN` clause
- 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드를 반환

### RIGHT JOIN syntax

``` SQL
SELECT
    select_list
FROM
    table1
RIGHT [OUTER] JOIN table2
    ON table1.fk = table2.pk;
```

- FROM 절 이후 왼쪽 테이블 지정 (table1)
- RIGHT JOIN 절 이후 오른쪽 테이블 지정 (table2)
- ON 키워드 이후 조인 조건을 작성
    - 오른쪽 테이블의 각 레코드를 왼쪽 테이블의 모든 레코드와 일치시킴

### RIGHT JOIN 예시

``` SQL
SELECT *
FROM articles
RIGHT JOIN users
    ON articles.userId = users.id;
```

### RIGHT JOIN 특징
- 오른쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시
- 오른쪽 테이블 한 개의 레코드에서 여러 개의 왼쪽 테이블 레코드가 일치할 경우, 해당 오른쪽 레코드를 여러 번 표시


### RIGHT JOIN practice #1
- 제시된 두 테이블을 참고하여 employees를 기준으로 employeeNumber 필드와 salesRepEmployeeNumber 필드가 일치하는 레코드와 함께 employeeNumber, firstName, customerNumber, contactFirstName 필드 조회
(왼쪽 테이블은 customers, 오른쪽 테이블은 employees, 일치하지 않는 경우 NULL)

``` SQL
SELECT employeeNumber, firstName, customerNumber, contactFirstName
FROM customers
RIGHT JOIN employees
	ON employees.employeeNumber = customers.salesRepEmployeeNumber;
```

### RIGHT JOIN practice #2
- 직전 조회 결과를 바탕으로 고객에게 판매한 내역이 없는 직원 목록 조회 (직원 번호와 이름은 employeeNumber, contactFirstName 필드이며 고객의 번호와 이름은 customerNumber, contactFirstName 필드)

``` SQL
SELECT employeeNumber, firstName, customerNumber, contactFirstName
FROM customers
RIGHT JOIN employees
	ON salesRepEmployeeNumber = employeeNumber
WHERE salesRepEmployeeNumber IS NULL;
```

