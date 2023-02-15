-- 생성

CREATE TABLE examples (
    examId INT AUTO_INCREMENT, -- 데이터 타입: INT, VACHAR(50)
    lastName VARCHAR(50) NOT NULL, -- 제약 조건: NOT NULL
    firstName VARCHAR(50) NOT NULL, -- 속성: AUTO_INCREMENT
    PRIMARY KEY (examId)
);

-- Table 구조 확인
SHOW COLUMNS FROM examples;

-- 삭제

DROP TABLE 
	examples;
    
-- 추가 #1

ALTER TABLE
	examples
ADD
	country VARCHAR(100) NOT NULL;


-- 추가 #2

ALTER TABLE
	examples
ADD
	age INT NOT NULL,
ADD
	address VARCHAR(100) NOT NULL;

-- 변경 #1

ALTER TABLE
	examples
MODIFY
	address VARCHAR(50) NOT NULL;

-- 변경 #2

ALTER TABLE
	examples
MODIFY lastName VARCHAR(10) NOT NULL,
MODIFY firstName VARCHAR(10) NOT NULL;

-- change 1

ALTER TABLE
	examples
CHANGE COLUMN country state VARCHAR(10) NOT NULL;

-- drop 1

ALTER TABLE
    examples
DROP COLUMN
    address;

-- drop 2
ALTER TABLE
    examples
DROP COLUMN
    state,
DROP COLUMN
    age;