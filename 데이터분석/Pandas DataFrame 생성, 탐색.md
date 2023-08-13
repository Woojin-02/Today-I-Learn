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
    * list(data) : 데이터프레임을 리스트 함수에 넣으면 열 이름이 리스트로반환
 * columns : 열 정보 확인
    * data.columns
 * dtypes : 열 자료형 확인
    * data.dtypes
 * info() : 열에 대한 상세한 정보 확인
    * data.Info()
 * describe() : 기초통계정보 확인
    * data.describe()
    * 개수(count), 평균(mean), 표준편차(std), 최솟값(min), 사분위 값(25%, 50%, 75%), 최댓값(max)