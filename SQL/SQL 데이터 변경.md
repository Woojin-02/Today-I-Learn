### SQL 데이터 변경

### 1. INSERT
* 테이블에 데이터를 삽입함
* 모든 열이 원래 순서대로 나열되는 경우 열 이름을 생략하기도 함
* 하지만 가독성 향상을 위해 열 이름을 지정하는 것이 좋음

```
-- 데이터 추가
INSERT INTO table(col1, col2, col3, col4)
    VALUES('이름', 1, 'A', '2023-10-01');
-- primary key를 기준으로 정렬되서 들어감

-- 열 이름 생략
INSERT INTO table
    VALUES('이름', 1, 'A', '2023-10-01');
```


### 2. UPDATE
* 테이블의 내용을 수정
* 되돌릴 수 없기 때문에 매우 주의해서 사용해야 함
* UPDATE문을 실행한 후에는 반드시 주석처리를 해둘 것
* MySQL 기준으로
* Edit - SQL edit 최하단에 safty를 풀지 않으면 WHERE절 없는 UPDATE문을 쓰는 경우 혹은 PRIMARY KEY를 WHERE절에 사용하지 않는 경우 에러 발생

```
UPDATE table
	SET phone = '010-1234-5678'
	WHERE name = '김연아';
```


### 3. DELETE
* 테이블의 내용을 삭제
* 되돌릴 수 없기 때문에 매우 주의해서 사용해야 함

```
-- 특정 조건에 맞는 행 지우기
DELETE FROM table
   WHERE date <= '2023-12-31';

-- 모든 행 지우기
DELETE FROM table;

-- 모든 행 지우기
-- 이게 더 빨리 처리됨
TRUNCATE TABLE table;
```