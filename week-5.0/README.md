### 要求⼀：安裝 MySQL 伺服器（省略）
---
### 要求⼆：建立資料庫和資料表

● 建立⼀個新的資料庫，取名為 website 。

● 在資料庫中，建立會員資料表，取名為 member 。

```sql
SHOW DATABASES;
CREATE DATABASE website;
USE website;
CREATE TABLE member(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
---
### 要求三：SQL CRUD

● 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
```sql
INSERT INTO member(name, username, password) VALUES('test', 'test', 'test');
INSERT INTO member(name, username, password, follower_count) VALUES('coco', 'coco', 'coco', 10);
INSERT INTO member(name, username, password, follower_count) VALUES('molly', 'molly', 'molly', 50);
INSERT INTO member(name, username, password, follower_count) VALUES('mars', 'mars', 'mars', 25);
INSERT INTO member(name, username, password, follower_count) VALUES('henry', 'henry', 'henry', 35);
```

![Q3-1](https://user-images.githubusercontent.com/110411867/196208108-ff4557bf-a1f5-4b93-b5d9-011191d98e9f.png)

● 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。

```sql
SELECT * FROM member;
```

![Q3-2](https://user-images.githubusercontent.com/110411867/196208116-b0420d3f-8a67-436a-9404-f8eb4808b49e.png)



● 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

```sql
SELECT * FROM member ORDER BY time DESC;
```

![Q3-3](https://user-images.githubusercontent.com/110411867/196208120-d798c0e8-cbb5-472e-9004-29f989657643.png)



● 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )

```sql
SELECT * FROM member ORDER BY time DESC LIMIT 1, 3;
```

![Q3-4](https://user-images.githubusercontent.com/110411867/196208122-057c3bf7-fb0f-48e8-a1d7-1cf94c20574c.png)



● 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。

```sql
SELECT * FROM member WHERE username='test';
```

![Q3-5](https://user-images.githubusercontent.com/110411867/196208124-3c72d23e-19d1-4f99-b0ab-5f037b128986.png)



● 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

```sql
SELECT * FROM member WHERE username='test' and password='test';
```

![Q3-6](https://user-images.githubusercontent.com/110411867/196208126-a20142a4-4d2d-4809-b584-49a124a6cd19.png)



● 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

```sql
SET SQL_SAFE_UPDATES=0;
UPDATE member SET name='test2' WHERE username='test';
```

![Q3-7](https://user-images.githubusercontent.com/110411867/196208129-49d1ba84-db25-4458-acad-ab5e92c6c82d.png)



---
### 要求四：SQL Aggregate Functions

● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

```sql
SELECT COUNT(*) FROM member; 
```

![Q4-1](https://user-images.githubusercontent.com/110411867/196208134-c8ef6c94-5f57-4799-b4a4-a66b9eb434c6.png)



● 取得 member 資料表中，所有會員 follower_count 欄位的總和。

```sql
SELECT SUM(follower_count) FROM member;
```

![Q4-2](https://user-images.githubusercontent.com/110411867/196208135-4bb9c0d6-4f59-46c0-9553-a60522b798ec.png)



● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

```sql
SELECT AVG(follower_count) FROM member;
```

![Q4-3](https://user-images.githubusercontent.com/110411867/196208138-74ba518e-4f0d-4d34-8369-e0f798ef1336.png)


---
### 要求五：SQL JOIN (Optional)

● 在資料庫中，建立新資料表紀錄留⾔資訊，取名為 message 。

```sql
CREATE TABLE message(
　id BIGINT PRIMARY KEY AUTO_INCREMENT,
  member_id BIGINT NOT NULL,
  content VARCHAR(255) NOT NULL,
  like_count INT UNSIGNED NOT NULL DEFAULT 0,
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO message(member_id, content, like_count) VALUES(3, 'Hello', 15);
INSERT INTO message(member_id, content, like_count) VALUES(1, 'Good Day', 0);
INSERT INTO message(member_id, content, like_count) VALUES(4, '嗨嗨', 12);
INSERT INTO message(member_id, content, like_count) VALUES(2, '早安安', 6);
INSERT INTO message(member_id, content, like_count) VALUES(1, 'testtest', 10);

SELECT * FROM message;
```

![Q5-1](https://user-images.githubusercontent.com/110411867/196208140-bd516f4b-bb82-4f2d-b653-9b7dc00560ed.png)



● 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。

```sql
ALTER TABLE message ADD FOREIGN KEY (member_id) REFERENCES member(id);
SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id;

```

![Q5-2](https://user-images.githubusercontent.com/110411867/196208143-9ae42e6d-4e86-4a7e-ba3e-c2037125a077.png)


```sql
SELECT * FROM member INNER JOIN message ON member.id=message.member_id;
 ```

![Q5-3](https://user-images.githubusercontent.com/110411867/196208148-233408a0-195e-4778-a849-94fd73e767bb.png)




● 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。

```sql
SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id WHERE member.username='test';
```

![Q5-4](https://user-images.githubusercontent.com/110411867/196208153-30f79210-481d-4edf-bbba-103034e228ef.png)


● 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。

```sql
SELECT AVG(like_count) FROM member INNER JOIN message ON member.id=message.member_id WHERE member.username='test';
```

![Q5-5](https://user-images.githubusercontent.com/110411867/196220023-9063a495-6100-462f-a0fa-7a67cee0d27c.png)
