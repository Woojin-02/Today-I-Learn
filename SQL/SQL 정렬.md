# SQL 정렬

- ORDER BY 절을 사용
- ASC: 오름차순  --> 1, 2, 3, 4 / 가, 나, 다, 라 / A, B, C, D
- DESC: 내림차순 --> 4, 3, 2, 1 / 라, 다, 나, 가 / D, C, B, A
- 정렬 방식을 생략하면 ASC가 지정된 것으로 간주됨
- 문자, 날짜, 숫자 모두 정렬 가능
- 복합 정렬은 콤마(,)로 구분해서 정렬 방식을 지정함

```
-- col1을 기준으로 먼저 정렬한 후에, col2를 기준으로 추가 정렬
-- col1은 ASC 방식으로 정렬(기본값 적용), col2는 DESC 방식으로 적용
SELECT *
	FROM table
	WHERE date IS NOT NULL
	ORDER BY col1, col2 DESC;  
```