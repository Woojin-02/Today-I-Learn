# SQL 하위쿼리

- 괄호 안에 또다른 쿼리문이 있는 쿼리문
- 대부분 JOIN 문으로 작성해서 같은 결과를 얻을 수 있음
- JOIN 문보다 작성하기가 쉬움

```
-- 가장 급여를 많이 받는 직원
SELECT emp_id, emp_name, dept_id, phone, email, salary
	FROM table
	WHERE salary = (SELECT MAX(salary) FROM table);

-- 하위 쿼리의 값이 여러개 나오면 IN을 사용할 수 있음
SELECT emp_id, emp_name, dept_id, phone, email, salary
	FROM table
	WHERE salary IN (SELECT MAX(salary) FROM table);  
```

### 상관 하위 쿼리
- 내부 쿼리(괄호 안에 있는 쿼리)가 독립적으로 수행되지 못함
- 외부 쿼리에서 넘겨진 값을 가지고 내부 쿼리가 수행됨

```
-- 부서 이름을 포함한 근무중인 직원 정보 조회
SELECT emp_id, emp_name, dept_id, 
       (SELECT dept_name FROM department WHERE dept_id = e.dept_id) AS dept_name, 
       phone, email, salary
	FROM employee AS e
	WHERE retire_date IS NULL;
```
* (SELECT dept_name FROM department WHERE dept_id = e.dept_id)
    * employee의 where절 조건에 맞는 dept_id와 일치하는 department의 부서 이름을 가져오기
    * 값이 하나가 나와야 함(dept_id가 primary 키 이기 때문에 하나만 나올 것이라고 확신할 수 있음)
    * 서브쿼리의 select 결과도 하나가 나와야 함, where의 = 결과도 하나가 나와야 함

#### EXISTS

* EXISTS : 조건에 맞는 데이터가 있는지 없는지만 확인
* INNER JOIN, IN, EXISTS중 EXISTS가 제일 빠름
* NOT EXISTS

```
-- 휴가를 간 적이 있는 근무중인 직원 정보 조회
-- EXISTS : *을 사용해도 괜찮음. * 말고 다른거 쓰지 말고 그냥 * 쓰기
SELECT emp_id, emp_name, dept_id, phone, email, salary
	FROM employee AS e
	WHERE EXISTS (
        SELECT *
            FROM vacation
            WHERE emp_id = e.emp_id
    ) AND retire_date IS NULL;
```
