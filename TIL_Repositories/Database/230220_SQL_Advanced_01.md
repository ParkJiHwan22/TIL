# SQL - Advanced 01

## 학습 목표

> Transaction을 사용하여 데이터베이스의 일관성을 보장할 수 있다.

> Trigger 작동 방식을 이해하고 작성하여 데이터 무결성을 보장할 수 있다.

# 01. Transactions
- 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법

### Transaction 예시
- 계좌이체(인출 & 입금)
    - 송금 중에 알 수 없는 문제로 인출에는 성공했는데 입금에 실패한다면...?
    - 인출과 입금 모두 성공적으로 끝나야 거래가 최종 승인되고, 중간에 문제가 발생한다면 거래를 처음부터 없었던 거래로 만들어야 함
    - 결국 함께 성공하던지 실패해야 함

### Transaction Syntax

``` SQL
START TRANSACTION;
INSERT INTO ... -- 임시 데이터 영역
state_ments;
...
[ROLLBACK|COMMIT]; -- COMMIT : 영구 데이터 영역
```

- START TRANSACTION: 트랜잭션 구문의 시작을 알림
- COMMIT: 모든 작업이 정상적으로 완료되면 한꺼번에 DB를 반영
- ROLLBACK: 부분적으로 작업이 실패하면 트랜잭션에서 진행한 모든 연산을 취소하고 트랜잭션 실행 전으로 되돌림

### Transaction practice #1
- 기본적으로 MySQL은 자동으로 변경 사항을 COMMIT함
- 변경 사항을 자동으로 COMMIT 하지 않도록 다음과 같이 설정

``` SQL
START TRANSACTION;
INSERT INTO users (name)
VALUES ('harry'), ('test');

SELECT * FROM users;

ROLLBACK;

SELECT * FROM users;
```

### Transaction 정리
- 쪼개질 수 없는 업무처리의 단위
- 전체가 수행되거나 또는 전혀 수행되지 않아야 함 (All or Nothing)

# 02. Triggers
- 특정 이벤트(INSERT, UPDATE, DELETE)에 대한 응답으로 자동으로 실행되는 것
- ~ 를 추가한 후에 ~ 하겠다.
- ~ 를 수정하기 전에 ~ 하겠다.
- ~ 를 삭제한 후에 ~ 하겠다.

### Triggers Syntax

``` SQL
CREATE TRIGGER trigger_name
    {BEFORE || AFTER} {INSERT | UPDATE | DELETE } -- Trigger는 DML의 영향을 받는 필드값에만 적용할 수 있음
    On table_name FOR EACH ROW
    trigger_body; 
```

- CREATE TRIGGER 키워드 다음에 생성하려는 트리거의 이름을 지정
- 각 레코드의 어느 시점에 트리거가 실행될지 지정(삽입, 수정, 삭제 전/후)
- ON 키워드 뒤에 트리거가 속한 테이블의 이름을 지정
- 트리거가 활성화될 때 실행할 코드를 trigger_body에 지정


### Triggers practice #1
- 트리거를 사용해 기존 게시글이 수정되면 게시글의 수정일자 필드 값을 최신 일자로 업데이트 하기

``` SQL
DELIMITER // -- 이 구간에 대한 종료 조건을 //로 설정한다.
CREATE TRIGGER myTrigger
	-- 언제?
	BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
    SET updatedAt = CURRENT_TIME();
END//
DELIMITER ;
```

- SQL의 구문 문자(;)를 변경
- BEGIN-END 구문 사이에 여러 SQL 문이 작성되기 때문에 하나의 트리거로써 작동될 수 있도록 사용
- 하나 이상의 구문 목록을 표현
- BEGIN과 END 키워드로 둘러싸는 다중 구문을 구성하게 됨

- 트리거에서 특점 시점 전/후의 값에 접근 할 수 있도록 제공하는 키워드
- OLD와 NEW 2개 제공
- 상황별로 사용할 수 있는 여부

    ||OLD|NEW|
    |--|--|--|
    |INSERT|NO|YES|
    |UPDATE|YES|YES|
    |DELETE|YES|NO|


### Triggers practice #2
- 트리거를 사용해 기존 게시글이 작성되면, 별도의 테이블에 해당 게시글이 작성되었다는 것을 기록하기

``` SQL
-- 사전 준비

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
```

### Triggers practice #2 심화
- 트리거를 사용해 기존 게시글이 작성되면, 별도의 테이블에 `몇 번` 게시글이 작성되었다는 것을 기록하기

``` SQL
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
```


### Triggers practice #3
- 트리거를 사용해 기존 게시글이 삭제되면, 삭제된 게시글의 구조 그대로 별도의 테이블에 기록하기

``` SQL
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
```

### Triggers 관련 추가 명령문

``` SQL
-- 트리거 목록 확인
SHOW TRIGGERS;

-- 트리거 삭제
DROP TRIGGER trigger_name;
```

### Triggers 생성 시 에러 해결
- 트랜잭션 생성 후 정상 적으로 종료되지 않아 발생하는 에러 발생 시 해결법

``` SQL
-- 실행 중인 프로세스 목록 확인
SELECT * FROM information_schema.INNODB_TRX;

-- 특정 프로세스의 trx_mysql_thread_id 삭제
KILL [trx_mysql_thread_id1];
```
