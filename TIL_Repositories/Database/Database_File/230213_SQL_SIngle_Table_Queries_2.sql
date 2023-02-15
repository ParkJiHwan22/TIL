SELECT DISTINCT
	lastName
FROM    
	employees
ORDER BY
	lastName;
    
-- Where 1

SELECT
	lastName, firstName, officeCode
FROM    
	employees
WHERE
	officeCode = 1;

-- Where 2
SELECT
	lastName, firstName, jobTitle
FROM
	employees
WHERE
	jobTitle != 'Sales Rep';

-- Where 3
SELECT
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode >= 3
	AND jobTitle = 'Sales Rep';

-- Where 4
SELECT
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode < 5
	OR jobTitle != 'Sales Rep';

-- Where 5
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode BETWEEN 1 AND 4;
    
-- Where 6
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode BETWEEN 1 AND 4
ORDER BY
	officeCode;
    
-- Where 7
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode IN (1, 3, 4);
    
-- Where 8
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode NOT IN (1, 3, 4);

-- Where 9
SELECT
	lastName, firstName
FROM 
	employees
WHERE 
	lastName LIKE '%son';

-- Where 10
SELECT
	lastName, firstName
FROM 
	employees
WHERE 
	firstName LIKE '___y';

-- LIMIT 1
SELECT
	firstName, officeCode
FROM
	employees
ORDER BY
	officeCode DESC
LIMIT 7;

-- LIMIT 2
SELECT
	firstName, officeCode
FROM
	employees
ORDER BY
	officeCode DESC
LIMIT 3, 5;

-- GROUP BY 1
SELECT
	country, AVG(creditLimit) AS avgOfCreditLimit
FROM
	customers
GROUP BY
	country
ORDER BY
	AVG(creditLimit) DESC;

-- GROUP BY 2
SELECT
	country, AVG(creditLimit)
FROM
	customers
-- WHERE
-- 	AVG(creditLimit) > 80000
GROUP BY
	country
HAVING
	AVG(creditLimit) > 80000;

-- NULL이 오름차순에서는 가장 먼저 위치
SELECT
    postalCode
FROM
    customers
WHERE
	postalCode IS NOT NULL -- NULL 제외
ORDER BY
    postalCode;


