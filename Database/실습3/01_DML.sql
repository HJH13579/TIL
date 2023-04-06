-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT COUNT(*) FROM users;

SELECT AVG(balance) FROM users;

SELECT country, avg(balance) FROM users
WHERE country='전라북도';

SELECT country, avg(balance) FROM users
GROUP BY country ORDER BY avg(balance) DESC;

SELECT last_name, COUNT(*)AS number_of_name FROM users
GROUP BY last_name;


CREATE table classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');

UPDATE classmates
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid=2;

DELETE FROM classmates
WHERE rowid = 5;

SELECT rowid, * FROM classmates;

DELETE FROM classmates
WHERE name LIKE '%영%';

SELECT rowid, * FROM classmates;

-- DROP TABLE 이 아니라 테이블 내의 데이터를 날리는 것

DELETE FROM classmates;

