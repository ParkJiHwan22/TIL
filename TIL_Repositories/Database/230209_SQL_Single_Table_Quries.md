# SQL -Single Table Quries

## 학습 목표

> 단일 테이블 내에서 SELECT문을 사용하여 테이블의 특정 결과를 반환할 수 있다.

> SELECT문과 함께 다양한 절을 사용해 쿼리 결과를 정렬 및 필터링 할 수 있다.

> GROUP BY와 Aggregation Function을 사용해 각 데이터 값에 대한 계산된 단일 값을 그룹화하여 반환할 수 있다.

## **`1. Querying data`**
- SELECT statement: 테이블에서 데이터를 조회

``` SQL
SELECT
    select_list
From
    table_name;
```

- SELECT 키워드 다음에 데이터를 선택하려는 필드를 하나 이상 지정
- FROM 키워드 다음에 데이터를 선택하려는 테이블의 이름을 지정

### SELECT examples #1
- 테이블 employees에서 lastName 필드의 모든 데이터를 조회

``` SQL
SELECT
    lastName
From
    employees;
```

### SELECT examples #2
- 테이블 employees에서 lastName, firstName 필드의 모든 데이터를 조회

``` SQL
SELECT
    lastName, firstName
From
    employees;
```

### SELECT examples #3
- 테이블 employees에서 모든 필드의 데이터를 조회

``` SQL
SELECT
    *
From
    employees;
```

### SELECT examples #4
- 테이블 employees에서 firstName 필드의 데이터를 조회
(단, 조회 시 firstName이 아닌 '이름'으로 출력될 수 있도록 출력명 변경)

``` SQL
SELECT
    firstName AS '이름'
From
    employees;
```

- `AS` Keyword: 필드에 새로운 별칭을 지정

### SELECT examples #5
- 테이블 orderdetails에서 ProductCode, 주문 총액 필드의 모든 데이터를 조회
(단, 주문 총액 필드는 quantityOrdered와 priceEach 필드를 곱한 결과 값)

``` SQL
SELECT
	ProductCode,
    quantityOrdered * priceEach AS '주문 총액'
From
    orderdetails;
```

- `Arithmetic Operators`: 기본적인 사칙연산 사용 가능

### SELECT 정리
- SELECT 문을 사용하여 테이블의 데이터를 조회 및 반환
- SELECT * (asterisk)를 사용하여 테이블의 모든 필드 선택

## **`2. Sorting data`**
- ORDER BY cluase: 조회 결과의 레코드를 정렬

``` SQL
SELECT
    select_list
FROM
    table_name
ORDER BY
column1 [ASC|DESC],
column2 [ASC|DESC],
...;
```

- FROM caluse 뒤에 위치
- 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬할 수 있음
    - ASC: 오름차순 (기본 값)
    - DESC: 내림차순

### ORDER BY examples #1
- 테이블 employees에서 firstNAME 필드의 모든 데이터를 오름차순으로 조회

``` SQL
SELECT
	firstName
FROM
	employees
ORDER BY
	firstName ASC; # ASC 안써도 됨, 기본값
```

### ORDER BY examples #2
- 테이블 employees에서 firstNAME 필드의 모든 데이터를 내림차순으로 조회

``` SQL
SELECT
	firstName
FROM
	employees
ORDER BY
	firstName DESC;
```

### ORDER BY examples #3
- 테이블 employees에서 lastName 필드를 기준으로 내림차순으로 정렬한 다음 firstNAME 필드 기준으로 오름차순으로 조회

``` SQL
SELECT
	lastName, firstName
FROM
	employees
ORDER BY
	lastName DESC,
	firstName ASC;
```

- lastName을 기준으로 정렬하고, 그 안에서 정렬할 수 있는 것들(필드명이 같은 경우)을 정렬함

### ORDER BY examples #4
- 테이블 orderdetails에서 totalSales 필드를 기준으로 내림차순으로 정렬한 다음 productCode, totalSales 필드의 모든 데이터를 조회
(단, totalSales 필드는 quantityOrdered와 priceEach 필드를 곱한 결과 값)

``` SQL
SELECT
	productCode,
    quantityOrdered * priceEach AS totalSales
FROM
	orderdetails
ORDER BY
	totalSales DESC;
```

## SELECT statement 실행 순서
- FROM -> SELECT -> ORDER BY
1. 테이블에서 (FROM)
2. 조회하여 (SELECT)
3. 정렬 (ORDER BY)