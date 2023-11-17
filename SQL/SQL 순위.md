# SQL 순위

### 1. RANK()
* 1, 2, 2, 4, ...
* 인원수가 꼴등의 등수가 되는 경우
* 1부터 n까지 숫자가 띄엄띄엄한 경우도 있음

```
-- 월급 순위 조회
SELECT col1, col2, col3, col4, salary,
       RANK() OVER(ORDER BY salary DESC) AS rnk
   FROM table;

-- 그룹별(남녀별) 월급 순위 조회 : PARTITION BY
SELECT col1, col2, col3, col4, salary,
       RANK() OVER(PARTITION BY gender ORDER BY salary DESC) AS rnk
   FROM table;
```

### 2. DENSE_RANK()
* 1, 2, 2, 3, ...
* 1부터 끝까지 순서대로 채워져있음
```
-- 전체 순위 조회
SELECT col1, col2, col3, col4, date,
	   DENSE_RANK() OVER(ORDER BY date DESC) AS rnk
   FROM table;

-- 마찬가지로 PARTITION BY 사용 가능
```


### 3. ROW_NUMBER()
* 1, 2, 3, 4, ...
* 같은 숫자가 절대 나오지 않음
* 순위는 아니고 번호를 매기는 것
* 숫자가 있으면 1~10, 11~ 20 처럼 분류할 수 있음 = 페이징
* 기준이 되는 값 중 중복되는 값이 있을 때는 알아서 번호를 매김
* 정렬을 이용해서 원하는 대로 중복되는 값이 있을 때의 번호를 어떻게 매길지 결정할 수 있음

```
-- 페이징 예시(하위 쿼리로 활용) : 6~10번까지 출력
SELECT * 
	FROM (
		SELECT ROW_NUMBER() OVER(ORDER BY col1 ASC) AS num,
				col1, col2, col3, col4
		FROM table
		WHERE col2 IS NULL) AS T
	WHERE num BETWEEN 6 AND 10;


-- 중복되는 값이 있을 때
SELECT ROW_NUMBER() OVER(ORDER BY col1 ASC, col2 DESC) AS num,
       col1, col2, col3, col4
   FROM table;
```


### 4. NTILE(n)
* 데이터를 n등분해서 순위를 결정
* NTILE(3) => 1, 1, 1, 2, 2, 2, 3, 3, 3
* n등분 시 나머지가 남으면 1위부터 하나씩 배분
    * 16을 3으로 나누면 6, 5, 5, 17을 3으로 나누면 6, 6, 5
* 정렬을 이용해서 원하는 대로 중복되는 값이 있을 때의 번호를 어떻게 매길지 결정할 수 있음

```
-- NTILE 사용
SELECT col1, col2, col3, col4
	   NTILE(3) OVER(ORDER BY col1 DESC, col3 ASC) AS grp
   FROM table;

-- 급여 순으로 3등분 (ELT를 사용해서 상/중/하로 구분하기)
SELECT col1, col2, col3, col4, salary,
	   ELT(NTILE(3) OVER(ORDER BY salary DESC), '상', '중', '하') AS grp
   FROM table;
```

**ELT 함수**
* 1을 넣으면 'A', 2를 넣으면 'B', 3을 넣으면 'C' 출력
* 개수가 안맞으면(범위 바깥의 숫자를 넣으면) NULL이 출력 (4를 넣거나 하는 등)
```
SELECT ELT(1, 'A', 'B', 'C')  =>  A
SELECT ELT(2, 'A', 'B', 'C')  =>  B
SELECT ELT(3, 'A', 'B', 'C')  =>  C
SELECT ELT(4, 'A', 'B', 'C')  =>  NULL
SELECT ELT(5, 'A', 'B', 'C')  =>  NULL
```