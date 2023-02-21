DROP TABLE users;

SET autocommit = 0;

CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    PRIMARY KEY (id)
);


-- Transaction practice #1
-- 기본적으로 MySQL은 자동으로 변경 사항을 COMMIT함
-- 변경 사항을 자동으로 COMMIT 하지 않도록 다음과 같이 설정

START TRANSACTION;
INSERT INTO users (name)
VALUES ('harry'), ('test');

SELECT * FROM users;

ROLLBACK;

SELECT * FROM users;


-- Triggers practice #1
-- 트리거를 사용해 기존 게시글이 수정되면 게시글의 수정일자 필드 값을 최신 일자로 업데이트 하기

DROP TABLES articles;

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

SELECT * FROM articles;

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

DELIMITER // -- 이 구간에 대한 종료 조건을 //로 설정한다.
CREATE TRIGGER myTrigger
	-- 언제?
	BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
    SET updatedAt = CURRENT_TIME();
END//
DELIMITER ;

UPDATE articles
SET title = 'new title'
WHERE id = 1;



-- Triggers practice #2
-- 트리거를 사용해 기존 게시글이 작성되면, 별도의 테이블에 해당 게시글이 작성되었다는 것을 기록하기

CREATE TABLE articleLogs (
    id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER recordLogs
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogs (description, createdAt)
    VALUES ('글이 작성 되었습니다.', current_time());
END//
DELIMITER ;

-- 풀이 확인

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articleLogs;


-- Triggers practice #2 심화
-- 트리거를 사용해 기존 게시글이 작성되면, 별도의 테이블에 `몇 번` 게시글이 작성되었다는 것을 기록하기

DELIMITER //
CREATE TRIGGER recordLogs
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogs (description, createdAt)
    VALUES (CONCAT(NEW.id, '번 글이 작성되었습니다.'), current_time());
END//
DELIMITER ;

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articleLogs;


-- Triggers practice #3
-- 트리거를 사용해 기존 게시글이 삭제되면, 삭제된 게시글의 구조 그대로 별도의 테이블에 기록하기

-- 사전 준비

CREATE TABLE backupArticles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER backupLogs
	AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO backupArticles (title, createdAt, updatedAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updatedAt);
END//
DELIMITER ;

-- 풀이 확인

DELETE FROM articles
WHERE id = 1;

SELECT * FROM backupArticles;

-- 트리거 목록 확인
SHOW TRIGGERS;

-- 트리거 삭제
DROP TRIGGER trigger_name;
DROP TRIGGER recordLogs;