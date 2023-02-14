# SQL - Modifying Data

## 학습 목표

> INSERT, UPDATE 그리고 DLELTE statement의 각 역할을 설명할 수 있다.

> 주어진 예시에 맞추어 테이블에 새로운 정보를 쓰거나 기존 레코드를 수정 및 삭제 할 수 있다.

# 1. Insert data into table

## `INSERT` statement
- 테이블 레코드 삽입

### INSERT syntax

``` SQL
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...);
```

- INSERT INTO절 다음에 테이블 이름과 괄호 안에 필드 목록을 작성
-VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록을 작성

### 예제 테이블 생성

``` SQL
CREATE TABLE articles (
    id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt DATE NOT NULL,
    PRIMARY KEY (id)
);

SHOW COLUMNS FROM articles;
```

### INSERT practice #1
- articles 테이블에 각 필드에 적합한 데이터 입력(단, createdAt 필드 값은 2000년 1월 1일이며 title과 content 필드 값은 자율)

``` SQL
INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('hello', 'world', '2000-01-01');
```


### INSERT practice #2
- articles 테이블에 각 필드에 적합한 데이터를 3개 입력(단, 모든 필드 값은 자율)

``` SQL
INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');
```

### INSERT practice #3
- articles 테이블에 각 필드에 적합한 데이터 입력(단, createdAt 필드에는 현재 작성하는 날짜가 자동으로 입력 나머지 필드 자율)

``` SQL
INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('hello', 'mycontent', CURDATE());
```

# 2. Update data in table

## `UPDATE` statement
- 테이블 레코드 수정

### UPDATE syntax

``` SQL
UPDATE table_name
SET column_name = expression,
[WHERE
    condition];   
```

- SET 절 다음에 수정 할 필드와 새 값을 지정
- WHERE 절에서 수정 할 레코드를 지정하는 조건 작성
    - WHERE 절을 작성하지 않으면 모든 레코드를 수정

### UPDATE practice #1
- articles 테이블 1번 레코드의 title 필드 값을 'new Title'로 변경

``` SQL
UPDATE articles
SET title = 'newTitle'
WHERE
    id = 1;   
```

### UPDATE practice #2
- articles 테이블 2번 레코드의 title, content 필드 값을 자유롭게 변경

``` SQL
UPDATE articles
SET title = 'newTitle', 
    content = 'newContent'
WHERE
    id = 2;  
```

### UPDATE practice #3
- articles 테이블 모든 레코드의 content 필드 값 중 문자열 'content'를 'TEST'로 변경

``` SQL
UPDATE articles
SET
    content = REPLACE(content, 'content', 'TEST');  
```

# 3. Delete data from table

## `DELETE` statement
- 테이블 레코드 삭제

``` SQL
DELETE FROM table_name
[WHERE
    condition];
```

- DELETE FROM 절 다음에 테이블 이름 작성
- WHERE 절에서 삭제할 레코드를 지정하는 조건 작성
    - WHERE 절을 작성하지 않으면 모든 레코드를 삭제

### DELETE practice #1
- articles 테이블 1번 레코드 삭제

``` SQL
DELETE FROM 
    articles
WHERE
    id = 1;
```

### DELETE practice #2
- articles 테이블에서 가장 최근에 작성된 레코드 2개를 삭제

``` SQL
DELETE FROM 
    articles
ORDER BY
    createdAt DESC
LIMIT 2;
```