CREATE TABLE articles (
    id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt DATE NOT NULL,
    PRIMARY KEY (id)
);

SHOW COLUMNS FROM articles;

SELECT * FROM articles;


-- Insert #1
INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('hello', 'world', '2000-01-01');


-- Insert #2
INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');


-- Insert #3
INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('hello', 'mycontent', CURDATE());
    
    
    