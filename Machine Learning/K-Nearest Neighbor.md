#  K-Nearest Neighbor

* ***회귀, 분류 모델 모두 사용 가능***

```python
# 회귀 모델 구현
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 분류 모델 구현
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
```

### 1. KNN

1. K-Nearest Neighbor
* 매우 간단함
* 테스트 데이터와 가장 가까운 이웃 k개의 값을 보고 예측값을 결정함
* 학습용 데이터 학습
* 학습한 데이터에서 k개의 최근접 이웃의 값을 찾아 새로운 값을 예측
    * 회귀 : 테스트 데이터와 가장 가까운 k개의 값의 평균을 계산
    * 분류 : 테스트 데이터와 가장 가까운 k개의 값이 가장 많은 유형으로 예측

2. **k값의 중요성**
* 탐색하는 이웃에 따라 데이터를 다르게 예측할 수도 있음
    * 주변 3개 탐색시 1이 2개면 예측값 = 1
    * 주변 5개 탐색시 0이 3개면 예측값 = 0
* k의 기본값은 5
* `n_neighbors` 옵션으로 k 값을 바꿀 수 있음
* k를 1로 설정하지 않고, 홀수로 설정하는 경우가 많음

### 2. Scaling
* K-Nearest Neighbor는 거리를 재기 때문에 x변수들의 범위가 다르면 정확한 결과가 나오지 않을 수 있음
* 때문에 스케일링이 필요
* ***평가용 데이터에도 학습용 데이터를 기준을 스케일링을 수행함***
    * 이렇게 해야만 올바른 결과 예측 가능
    * 만약 평가용 데이터가 학습용 데이터와 범위가 다르다면 어쩔 수 없음
* 모든 작업을 다 끝내고, 분석도 다 하고 머신러닝을 실행 하기 전에 시행해야 함


1. 표준화(Standaredization)
* 각 변수의 평균이 0, 표준편차가 1
* x = (x-x.mean) / x.std

2. 정규화(Normalization)
* 각 변수의 값이 0과 1 사이 값
* x = (x-x.min) / (x.max-x.min)
* 공식을 사용(df로 리턴)하거나, 함수 사용(array로 리턴)

```python
#함수 불러오기
from sklearn.preprocessing import MinMaxScaler

#정규화
scaler = MinMaxScaler() 
scaler.fit(x_train) # 학습용 데이터의 minmax값을 가지고 있음
x_train= scaler.transform(x_train)
x_test= scaler.transform(x_test)
```

### 3. n_neighbors 옵션