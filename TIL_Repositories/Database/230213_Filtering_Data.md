# SQL -Single Table QuriesⅡ

## 학습 목표

> 단일 테이블 내에서 SELECT문을 사용하여 테이블의 특정 결과를 반환할 수 있다.

> SELECT문과 함께 다양한 절을 사용해 쿼리 결과를 정렬 및 필터링 할 수 있다.

> GRUUP BY와 Aggregation Function을 사용해 각 데이터 값에 대한 계산된 단일 값을 그룹화하여 반환할 수 있다.

# 3. Filtering data
- Fitering data 관련 Keywords

|키워드|종류|
|--|--|
|Clause|DISTINCT, WHERE, LIMIT|
|OPERATOR|BETWEEN, IN, LIKE, Comparison, Logical|

## `DISTINCT` clause
- 조회 결과에서 중복된 레코드를 제거

``` SQL
SELECT DISTINCT
    select_list
FROM
    table_name;
```

- SELECT 키워드 바로 뒤에 작성해야 함
- SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정

### DISTINCT practice #1
- 테이블 employees에서 lastName 필드의 모든 데이터를 중복없이 오름차순 조회

``` SQL
SELECT DISTINCT
	lastName
FROM
	employees
ORDER BY
	lastName;
```	

## `WHERE` clause
- 조회 시 특정 검색 조건을 지정

``` SQL
SELECT
    select_list
FROM
    table_name
WHERE
    search_condition;
```

- FROM clause 뒤에 위치
- search_condition은 비교연산자 및 논리연산자(AND, OR, NOT 등)를 사용하는 구문이 사용됨

### WHERE practice #1
- 테이블 employees에서 officeCode 필드 값이 1인 데이터의 lastName, firstName, officeCode 조회

``` SQL
SELECT
	lastName, firstName, officeCode
FROM    
	employees
WHERE
	officeCode = 1;
```

### WHERE practice #2
- 테이블 employees에서 job Title 필드 값이 'Sales Rep'이 아닌 데이터의 lastName, firstName, jobTitle 조회

``` SQL
SELECT
	lastName, firstName, jobTitle
FROM
	employees
WHERE
	jobTitle != 'Sales Rep';
```

### WHERE practice #3
- 테이블 employees에서 officeCode 필드 값이 3 이상이고 jobTitle 필드 값이 'Sales Rep'인 데이터의 lastName, firstName, officeCode, jobTitle 조회

``` SQL
SELECT
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode >= 3
	AND jobTitle = 'Sales Rep'; -- AND로 조건을 묶었다 , 아님
```

### WHERE practice #4
- 테이블 employees에서 officeCode 필드 값이 5 미만이거나 jobTitle 필드 값이 'Sales Rep'이 아닌 데이터의 lastName, firstName, officeCode, jobTitle 조회

``` SQL
SELECT
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode < 5
	OR jobTitle != 'Sales Rep';
```

### WHERE practice #5
- 테이블 employees에서 officeCode 필드 값이 1에서 4 사이 값인 데이터의 lastName, firstName, officeCode 조회 (1과 4를 포함)

``` SQL
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode BETWEEN 1 AND 4; -- BETWEEN
```

### WHERE practice #6
- 테이블 employees에서 officeCode 필드 값이 1에서 4 사이 값인 데이터의 lastName, firstName, officeCode를 오름차순 조회 (1과 4를 포함)

``` SQL
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode BETWEEN 1 AND 4
ORDER BY
	officeCode; -- ORDER BY의 위치 확인하기
```

### WHERE practice #7
- 테이블 employees에서 officeCode 필드 값이 1 또는 3또는 4 값인 데이터의 lastName, firstName, officeCode를 조회

``` SQL
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode IN (1, 3, 4);
```

### WHERE practice #8
- 테이블 employees에서 officeCode 필드 값이 1과 3 그리고 4가 아닌 데이터의 lastName, firstName, officeCode를 조회

``` SQL
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode NOT IN (1, 3, 4);
```

### WHERE practice #9
- 테이블 employees에서 lastName 필드 값이 son으로 끝나는 데이터의 lastName, firstName 조회

``` SQL
SELECT
	lastName, firstName
FROM 
	employees
WHERE 
	lastName LIKE '%son';
```



### WHERE practice #10
- 테이블 employees에서 firstName 필드 값이 4자리면서 y로 끝나는 데이터의 lastName, firstName 조회

``` SQL
SELECT
	lastName, firstName
FROM 
	employees
WHERE 
	firstName LIKE '___y';
```

### Comparison Operators
- 비교 연산자
- =, >=, <=, !=, IS, LIKE, IN, BETWEEN...AND

### Logical Operators
- 논리 연산자
- AND(&&), OR(||), NOT(!)

### `IN` operators
- 값이 특정 목록 안에 있는지 확인

### `LIKE` operator
- 값이 특정 패턴에 일치하는지 확인 with Wildcards

### Wildcard Characters
- '%': `0개 이상의 문자열`과 일치하는지 확인
- '_': `단일 문자`와 일치하는지 확인

### LIMIT syntax
- 조회하는 레코드 수를 제한

``` SQL
SELECT
    select_list
FROM
    table_name
LIMIT [offset,] row_count;
```
- LIMIT clause는 하나 또는 두 개의 인자를 사용 (0 또는 양의 정수)
- row_count는 조회할 최대 레코드 수를 지정

### LIMIT practice #1
- 테이블 employees에서 firstName, officeCode 필드 데이터를 officeCode 기준 내림차순으로 7개만 조회

``` SQL
SELECT
	firstName, officeCode
FROM
	employees
ORDER BY
	officeCode DESC
LIMIT 7;
```

### LIMIT practice #2
- 테이블 employees에서 firstName, officeCode 필드 데이터를 officeCode 기준 내림차순으로 4번째부터 8번째 데이터만 조회

``` SQL
SELECT
	firstName, officeCode
FROM
	employees
ORDER BY
	officeCode DESC
LIMIT 3, 5;
```

# 4. Grouping data

### `GROUP BY` clause
- 레코드를 그룹화하여 요약본 생성 with `집계 함수`
- Aggregation Functions: 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
    - SUM, AVG, MAX, MIN, COUNT
- GROUP BY syntax

``` SQL
SELECT
    c1, c2, ..., cn, aggregate_function(ci)
FROM
    table_name
GROUP BY
    c1, c2, ..., cn;
```
- FROM 및 WHRER 절 뒤에 배치
- GROUP BY 절 뒤에 그룹화할 필드 목록을 작성

### GROUP BY 이해하기
- jobTitle 필드를 그룹화

``` SQL
SELECT
    jobTitle
FROM
    employees
GROUP BY
    jobTitle; -- SELECT에서 DISTINCT 한 것과 같음
```

- COUNT 함수가 각 그룹에 대한 집계된 값을 계산

``` SQL
SELECT
    jobTitle, COUNT(*)
FROM
    employees
GROUP BY
    jobTitle;
```

GROUP BY practice #1
= 테이블 customers에서 country필드를 그룹화하여 각 그룹에 대한 creditLimit의 평균 값을 내림차순 조회

``` SQL
SELECT
	country,
    AVG(creditLimit)
FROM
	customers
GROUP BY
	country
ORDER BY
	AVG(creditLimit) DESC;
```

GROUP BY practice #2
- 테이블 customers에서 country필드를 그룹화하여 각 그룹에 대한 creditLimit의 평균 값이 800000을 초과하는 데이터만 조회

``` SQL
SELECT
	country, AVG(creditLimit)
FROM
	customers
-- WHERE
-- 	AVG(creditLimit) > 80000
GROUP BY
	country
HAVING
	AVG(creditLimit) > 80000; -- HAVING clause: 집계 항목에 대한 세부 조건을 지정
```

### SELECT statement 실행 순서
1. 테이블에서(FROM)
2. 특정 조건에 맞춰(WHERE)
3. 그룹화하고(GROUP BY)
4. 만약 그룹 중에서 조건이 있다면 맞추고(HAVING)
5. 조회하여 (SELECT)
6. 정렬하고 (ORDER BY)
7. 특정 위치의 값을 가져온다 (LIMIT)

### 정렬에서의 NULL
- MySQL에서 NULL은 NULL이 아닌 값 앞에 위치
    - NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력

``` SQL
-- NULL 정렬 예시
SELECT
    postalCode
FROM
    customers
ORDER BY
    postalCode;
```