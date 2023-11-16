# SQL 기본

### 기본 문법
1. 문자열 출력 : `SELECT 'Hello SQL World';`
2. 별칭 사용 : `SELECT 'Hello SQL World' AS Hello;`
3. 숫자 연산 결과 출력 : `SELECT 10 + 20;`
4. 함수 결과 출력 : `SELECT CURDATE() AS Today;`
5. 변수 값 설정: `SET @Today = CURDATE();`
6. 변수 값 출력 : `SELECT @Today;`
7. 데이터베이스 연결 : `USE DB이름`
8. 현재 데이터베이스 확인 : `SELECT DATABASE();`

### SELECT 
* 기본 형태 : table의 모든 정보를 가져오기
```
 SELECT * 
	FROM table명;
```

* 일부만 가져오기
```
-- 테이블에서 특정 컬럼만 가져오기
SELECT col1, col2
	FROM table명;

-- 테이블에서 일부 행만 가져오기
SELECT *
	FROM table명
	WHERE col1 = 'M' AND col2 >= 1000;  -- AND를 사용하면 조건을 여러개 걸 수 있음

-- 테이블의 일부 행과 열만 가져오기
-- table에서 col1이 'M'인 col1, col2 열과 행을 가져오기
SELECT col1, col2
	FROM table명
	WHERE col1 = 'M';
```

* LIKE 연산자
    * WHERE절에 문자%, %문자, %문자%를 이용해 조회 가능
    * 문자% : 문자로 시작하는 데이터
    * %문자 : 문자로 끝나는 데이터
    * %문자% : 문자를 포함하는 데이터
    * _ : 개수 지정('__문자'는 문자 앞에 단어가 __의 개수(2개)만큼만 있는 데이터를 조회)
* NOT LIKE 연산자
    * 반대로 적용
    * ex) `WHERE col1 NOT LIKE 'a%'` 일 경우 a로 시작하지 않는 모든 문자열 조회
```
-- 전화번호가 017로 시작
SELECT *
	FROM table명
	WHERE phone LIKE '017%';

--  전화번호가 010으로 시작하지 않는
SELECT *
	FROM table명
	WHERE phone NOT LIKE '010%';
```

* 논리 연산자: AND, OR, NOT
    * AND는 조건을 만족할 수록 결과 행이 줄어듦(긍정적)
    * OR는 조건을 만족할 수록 결과 행이 늘어남(부정적)
    * NOT은 조건에 대한 부정을 의미함
```
SELECT *
	FROM table명
	WHERE date >= '2016-01-01' AND date <= '2016-12-31';
```

* 범위 조건(BETWEEN)과 리스트 조건(IN)
    * BETWEEN : A <=  <= B
    * NOT BETWEEN : A> ,  B<
    * IN
    * NOT IN
```
-- 2016년 정보 조회
SELECT *
	FROM table명
	WHERE date BETWEEN '2016-01-01' AND '2016-12-31'; 

-- 2016년 외에 정보 조회
SELECT *
	FROM table명
	WHERE date NOT BETWEEN '2016-01-01' AND '2016-12-31';

-- col1이 A, B, D인 정보 조회
SELECT *
	FROM table명
	WHERE col1 IN ('A', 'B', 'D');

-- col1이 A, B, D가 아닌 정보 조회
SELECT *
	FROM table명
	WHERE col1 NOT IN ('A', 'B', 'D');
```

* NULL
    * IS NULL
    * IS NOT NULL
    * COALESCE() 함수 : 나열된 값 중에서 첫 번째 NULL이 아닌 값
        * 모든 SQL 도구에서 공통적으로 사용
```
-- NULL 조회
SELECT *
	FROM table명
	WHERE col1 IS NULL;
    
-- NULL이 아니면 조회
SELECT *
	FROM table명
	WHERE col1 IS NOT NULL;

-- COALESCE()를 이용해 NULL 값 변경
SELECT COALESCE(col3, '') AS col3_change_null  -- col3에 있는 NULL을 공백으로 바꿈
	FROM table명

```

