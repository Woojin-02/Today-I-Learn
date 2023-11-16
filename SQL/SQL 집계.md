# SQL 집계

### 집계 함수: SUM, AVG, MAX, MIN, COUNT
- 합, 평균값, 최댓값, 최솟값, 개수를 구함
- 합과 평균값은 숫자에 대해서만 구할 수 있음
- 최댓값, 최솟값, 개수는 문자와 날짜에 대해서 사용 가능
- 날짜의 최솟값 = 가장 빠른(오래된) 날짜
- 날짜의 최댓값 = 가장 최근 날짜
- 행 수를 구할 때는 COUNT(*)를 사용함
- **모든 집계 함수는 NULL 값을 무시**
    - NULL값이 있는 열에 대한 집계 시 주의 필요
- **Count(*)의 경우만 예외**

```
-- 근무중인 직원의 급여 평균 조회
SELECT AVG(salary) AS avg_salary
	FROM employee
	WHERE retire_date IS NULL;  -- 결과 : 6060.0000, 15가 전체

-- 급여 합을 직원 수로 나눠서 급여 평균 조회
SELECT SUM(salary) / COUNT(*) AS avg_salary
	FROM employee
	WHERE retire_date IS NULL;  -- 결과 5681.2500, 16이 전체
```

### 그룹별 집계: GROUP BY
- 집계 기준열을 지정해 그룹별 집계를 할 수 있음
- 부서별, 남녀별, 지역별, 연도별 등등

```
SELECT col1, COUNT(*) AS count
	FROM table
	WHERE retire_date IS NULL
	GROUP BY col1;  -- groupby 절을 적용한 열과 COUNT(*)을 반드시 사용해야 함
```

### 집계 결과에 대한 조건: HAVING
- WHERE 절 조건: GROUP BY 하기 전 조건
- HAVING 절 조건: GROUP BY 한 후 조건
- HAVING 없는 GROUP BY는 존재할 수 있지만,
- GROUP BY 없는 HAVING은 존재할 수 없음

```
-- 근무중인 직원이 3명 이상인 부서별 근무중인 직원 수 조회
SELECT dept_id, COUNT(*) AS emp_count   -- 5)
	FROM employee   					-- 1)
	WHERE retire_date IS NULL   		-- 2)
	GROUP BY dept_id   					-- 3)
	HAVING COUNT(*) >= 3   				-- 4)
	ORDER BY emp_count DESC;   			-- 6)
```