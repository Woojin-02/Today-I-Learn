# 데이터 결합

- CONCAT 함수를 사용해 데이터 결합
- 결합되는 값에 NULL 값이 포함되면 결합 결과가 NULL이 됨

### 자동 형변환
* 그냥 숫자를 입력하면 자동으로 형변환이 됨
```
SELECT '10' + '20';  -- 30
SELECT 10 + '20';   -- 30
SELECT 10 + '20AX';  -- 30(10, 20만 인정, AX는 인정 안됨)
SELECT 10 + 'LX20';  -- 10(10만 인정, LX 이후로는 인정 안됨)
```

### 문자열 데이터 결합
* CONCAT 사용
```
SELECT CONCAT('10', '20');  -- '1020'
SELECT CONCAT(10, '20');  -- '1020'
SELECT CONCAT(10, 20);  -- '1020'
SELECT CONCAT(10, NULL);  -- NULL, NULL과의 연산은 전부 NULL
```

### 열 데이터 결합
* CONCAT 사용
```
SELECT CONCAT(col1, '(', col2, ')') AS col4
	FROM table
	WHERE date IS NOT NULL;
```