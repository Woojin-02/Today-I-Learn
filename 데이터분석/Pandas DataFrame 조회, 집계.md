# Pandas (DataFrame 조회, 집계)

### 1. 데이터프레임 조회
1. 1차원(시리즈)으로 조회
    * DataFrame['column']
    * DataFrame.column

2. 2차원(데이터프레임)으로 조회
    * DataFrame[['column']]
        * *칼럼 이름을 리스트로 입력!*

3. 조건으로 조회 : .loc[행 조건, 열 이름]
    * 행 조건 : 조건문
    * 열 이름 : 생략 가능, 열 이름이 1개면 시리즈로, 여러개면 리스트(데이터프레임)으로 결과 출력
    * 모든 행을 가져오려면 data.loc[ : , ['tax', 'Income']]
    * tax 열 값이 20보다 작은 행 조회 data.loc[data['tax'] < 20]

4. 여러 조건으로 조회
    * &(and) 와 |(or) 연산자를 사용하며, 각 조건은 소괄호로 묶어야 함
        * 반드시 and, or 대신 연산자를 사용
    * data.loc[(data['tax'] < 20) & (data['dat'] == 'Mon')]
    * data.loc[(data['tax'] < 20) | (data['dat'] == 'Mon')]
    </br>
    > isin(), between()
    >* isin([값1, 값2, ... , 값n]) : 여러개의 값 조회
    >   * data.loc[data['class'].isin(['1', '2']) </br>
         = data.loc[(data['class'] == 1) | (data['class'] == 2)]
    >   * 여러개의 | 연산자를 축약할 때 좋음
    >* between(값1, 값2) : 값1~값2 사이의 데이터만 조회
    >   * data.loc[data['Age'].between(15, 20)] </br>
         = data.loc[(data['Age'] >= 15) & (data['Age'] <= 20)]
    >   * inclusive : 이상, 이하, 미만, 초과 결정
    >       * both(기본값) : a <= , >= b 
    >       * left : a <= , > b 
    >       * right : a < , >= b 
    >       * neither : a < , > b 
    >       * data.loc[data['Age'].between(40, 50, inclusive='right')

5. 조건을 만족하는 행의 일부 열 조회
 * .loc[조건, ['열이름1', '열이름2', ...]]
    * data.loc[data['Age'] > 50, ['Gender']]
    * 나이가 50살 초과인 사람의 성별 조회

### 2. 데이터프레임 집계

* sum(), mean(), max(), min(), count() 메소드를 사용하여 열 또는 열들을 기준으로 집계
    * 평균은 avg()가 아닌 mean()

1. 특정 열의 집계
    * data['행 이름'].sum()
    * data[['행이름1', '행이름2']].sum()

2. ***groupby***
    * dataframe.groupby('집계기준변수', as_index=)['집계대상변수'].집계함수
        * 나이 별 월급 평균
        * 나이 : '집계기준변수', ~별에 해당되는 변수 혹은 리스트. 범주형 변수
        * 월급 : '집계대상변수', 집계함수로 집계할 변수 혹은 리스트
        * as_index = True : 집계기준변수를 인덱스로 사용
        * 집계대상변수를 []리스트로 감싸면 결과가 데이터프레임이 됨. 감싸지 않으면 시리즈가 됨
        * data.groupby('Age', as_index=False)['MonthIncome'].mean()
    * 여러 열 집계
        * 여러 집계 대상 : data.groupby('Age', as_index=False)[['MonthIncome', 'tax']].mean()
        * 여러 집계 기준 : data.groupby(['Age', 'Gender'], as_index=False)[['MonthIncome']].mean()
    * 여러 함수로 한꺼번에 집계 : .agg
        * data.groupby('Age', as_index=False)['MonthIncome'].agg['mean', 'count', 'max']
        * as_index = False 로 설정해도 집계기준변수를 인덱스로 사용

### 3.


### 4.


### 5.

