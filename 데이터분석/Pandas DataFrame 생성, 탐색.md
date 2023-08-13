# Pandas (DataFrame 생성, 탐색)

### 1. 데이터프레임(DataFrame)

 * 데이터 분석에서 가장 중요한 데이터 구조
 * 관계형 데이터베이스의 테이블 또는 엑셀 시트와 같은 2차원 구조 형태
 * 데이터 프레임에서 하나의 열을 떼어낸 것을 Series라고 부름(1차원)
    * Series의 모임 = DataFrame

```python
import pandas as pd
```

### 2. 데이터프레임 만들기
 1. pd.DataFrame()을 이용해서 딕셔너리를 데이터프레임으로 만들기

 2. csv 파일 불러오기
 ```python
 data = pd.read_csv('경로') 
```

### 3. 데이터프레임 정보 확인 메서드
 * head() : 상위 데이터 확인
    * data.head(10)
 * tail() : 하위 데이터 확인
    * data.tail(3)
 * shape : 데이터프레임 크기
    * (rows, cols)의 튜플 평태로 확인 가능
    * 데이터 양 확인 가능
    * data.shape
 * values : 값 정보 확인(저장하면 2차원 numpy 배열이 됨)
    * data.columns.values
    * list(data) : 데이터프레임을 리스트 함수에 넣으면 열 이름이 리스트로 반환
 * columns : 열 정보 확인
    * data.columns
 * dtypes : 열 자료형 확인
    * data.dtypes
 * info() : 열에 대한 상세한 정보 확인
    * data.Info()
 * describe() : 기초통계정보 확인
    * data.describe()
    * 개수(count), 평균(mean), 표준편차(std), 최솟값(min), 사분위 값(25%, 50%, 75%), 최댓값(max)


### 4. 데이터프레임 데이터 정렬
 * Sort_index : 인덱스를 기준으로 정렬
   * data.sort_index(ascending=False)
 * Sort_values : 특정 열을 기준으로 정렬
   * data.sort_values(by='기준 열', ascending=Falue)
   * data.sort_values(by=['기준 열1', '기준 열2'], ascending=[False, False])
      * 기준열 1을 우선으로 정렬하고, 다음으로 기준열 2번으로 정렬
      * ascending=True : 오름차순 정렬(기본값)
      * ascending=False : 내림차순 정렬
   * drop = True : 인덱스 재구성
      * data.reset_index(drop=True)

### 5. **기본 집계**
* 데이터를 좀 더 이해하기 위해 고유값, 합, 평균, 최댓값, 최소값 등을 확인

1. **고유값 확인**
 * 범주형 열인지 확인할 때 사용
 * unique() : 특정 열 고유값 확인. 결과값은 배열 형태가 된다.
   * data['특정 열 이름'].unique() -> ['male', 'Female']
 * **value_counts()** : 고유값과 그 개수 확인. 결과값은 시리즈 형태가 된다.
   * data['특정 열 이름'].value_counts() -> male : 200, Female : 150

2. 기본 집계 메소드
 * sum() : 열 합계
 * max() : 열 평균값
 * mean() : 열 평균값
 * median() : 열 중앙값
   * data[['Age', 'NumofVisit']].median()
   * data['Age'].mean()