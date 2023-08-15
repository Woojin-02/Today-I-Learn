# Pandas (DataFrame 결합)

### 1. concat

 * 매핑 기준 : 인덱스(행) 칼럼 이름(열)

1. axis = 0
    * **세로(행)로 합치기(행방향으로 합치기, 위아래로 붙여라)**
    * 칼럼 이름 기준
        * 칼럼 이름이 같은게 있는지 없는지로 inner 조인과 outer 조인의 결과가 달라짐
    * outer : 모든 행과 열 합치기 (기본값).
        * 칼럼 이름이 같으면 정상적으로 아래에 데이터프레임이 합쳐지고, 칼럼 이름이 다르면 Nan 생성
    * inner : 같은 행과 열만 합치기. 칼럼 이름이 같은 열끼리만 결합
    * pd.concat([df1, df2], axis = 0, join = 'inner')

2. axis = 1
    * **가로(열)로 합치기(열방향으로 합치기, 옆으로 붙여라)**
    * 행 인덱스 기준
        * 인덱스 이름이 같은게 있는지 없는지로 inner 조인과 outer 조인의 결과가 달라짐
    * outer : 모든 행과 열 합치기 (기본값)
        * 인덱스 이름이 같으면 정상적으로 아래에 데이터프레임이 합쳐지고, 인덱스 이름이 다르면 Nan 생성
    * inner : 같은 행과 열만 합치기.
    * pd.concat([df1, df2], axis = 1, join = 'inner')

### 2. merge
 * 매핑 기존 : 특정 칼럼(key)의 값 기준
 * 옆으로만 병합
 * 데이터베이스 테이블 조인과 같음
 * how(방법)
    * inner : 같은 값만 병합 ( 기본값 )
    * outer : 모두 병합
    * left : 왼쪽 df는 모두, 오른쪽 df는 값은 값만 병합 (왼쪽 df는 그대로 두고, 오른쪽 df 중 값만 같은 내용을 옆에 붙임)
    * right : 오른쪽 df는 모두, 왼쪽 df는 값은 값만 병합(오른쪽 df는 그대로 두고, 왼쪽 df 중 값만 같은 내용을 옆에 붙임)

* pd.merge(df1, df2, how = 'inner', on = '칼럼 이름')
    * inner를 사용하고, 이름이 서로 같은 칼럼이 있는 경우 how, on 생략 가능
    * df1의 A 칼럼과 df2의 A 칼럼 중에서 서로 값이 같은 경우 merge하는 것이 기본
    * outer, left, right의 경우 결측치(NaN)이 발생할 수 있음

#### 부록) pivot
 * 집계 후 데이터프레임 구조를 변형해서 조회하는데 종종 사용
 * df.pivot(index, column, values)
 * groupby를 사용 후에 pivot 사용
 * 예시
 ```python
temp = pd.merge(sales1, products)
temp2 = temp.groupby(['Date', 'Category'], as_index = False)['Qty'].sum()

temp3 = temp2.pivot( 'Category', 'Date' ,'Qty')
```
 * 시각화
 ```python
plt.figure(figsize = (20, 6))
sns.heatmap(temp3)
plt.show()
```