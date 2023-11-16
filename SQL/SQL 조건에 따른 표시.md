# SQL 조건 표시

### CASE 문
* 쿼리문 안에서 조건에 따라 다른 값을 표시할 수 있음
```
-- 성별: M, F --> 남자, 여자
SELECT name, id,
       CASE WHEN gender = 'M' THEN '남자'
            WHEN gender = 'F' THEN '여자'
            ELSE '' END AS gender,      
            -- M, F 이외의 성별이 입력될 경우를 처리해야 하기 때문에 ELSE '여자' 같은 식으로는 사용 금지
            -- 만약 ELSE를 생략하면 M, F 이외의 값이 들어올 경우 NULL이 됨
	FROM table;
```

### IF 함수
- IF(조건, 참일 때 값, 거짓일 때 값)
- 주어진 조건이 참인지 거짓인지에 따라 값을 선택
- 조건 하나에 따른 값 선택의 경우 CASE 문보다 사용이 용이
```
-- 성별: M, F --> 남자, 여자
SELECT name, id, 
       IF(gender = 'M', '남자', '여자') AS gender, 
	   date, salary
	FROM employee;
```