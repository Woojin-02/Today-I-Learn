# SQL 조인

### 1. INNER JOIN
- 가장 일반적인 JOIN 문 형태
- default 값이기 때문에 INNTER를 생략하고 JOIN만 사용해도 INNER JOIN이 사용됨
- 양쪽 테이블에서 비교되는 값이 일치하는 행만 가져옴
- 일반적으로 PK와 FK가 ON 절에서 서로 비교됨

```
SELECT d.dept_id, d.dept_name, d.unit_id, u.unit_name, d.start_date
	FROM department AS d
	INNER JOIN unit AS u ON d.unit_id = u.unit_id;
```


### 2. OUTER JOIN
- 비교되는 값이 일치하지 않는 행도 기준 테이블에서 가져옴
- LEFT OUTER JOIN, RIGHT OUTER JOIN, FULL OUTER JOIN
    - LEFT OUTER JOIN : 왼쪽 테이블을 기준으로 적용
    - RIGHT OUTER JOIN : 오른쪽 테이블을 기준으로 적용
- 단, MySQL은 FULL OUTER JOIN 이 없음

```
SELECT e.emp_id, e.emp_name, d.dept_name, u.unit_name, 
       v.begin_date, v.duration
   FROM employee AS e
   INNER JOIN department AS d ON e.dept_id = d.dept_id
   LEFT OUTER JOIN unit AS u ON d.unit_id = u.unit_id
   INNER JOIN vacation AS v ON e.emp_id = v.emp_id
   WHERE v.begin_date BETWEEN '2017-01-01' AND '2017-03-31'
   ORDER BY e.emp_id ASC;
```


### 3. CROSS JOIN
- 일반적인 비즈니스 응용프로그램에서 사용되지 않음
- ON 절이 없어 모든 경우의 수만큼 결과 행을 얻음 (카티션 곱)
- 대량의 테스트 데이터를 만드는 목적으로 많이 사용됨

```
SELECT emp_name, dept_name
    FROM employee AS e
    CROSS JOIN department AS d;
```


< 참고 > </br>
어떤 순서로 조인할 지는 MySQL 서버가 결정한다. </br>
사람은 어떤 테이블이 어떻게 조인 될 지만 작성해 주면 된다. </br>
실제 처리 방식은 가장 효율적인 방법을 서버가 찾아 수행한다.</br>
아니면 튜닝을 진행해서 최적의 경로를 설정하는 것을 도와준다.</br>