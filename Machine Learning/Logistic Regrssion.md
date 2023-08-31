# Logistic Regression

* ***분류 모델에서만 사용 가능***

```python
from sklearn.linear_model import LogisticRegrssion
from sklearn.metrics import confusion_matrix, classification_report
```

### 1. 언제 사용하는가
* 투자한 시간, 걸음 수 등 어떤 단계에 따라 0 또는 1의 결과가 나오는 문제에서 사용

### 2. 로지스틱 회귀
* 독립 변수의 선형 결합을 이용하여 사건의 발생 가능성을 예측하는 데 사용되는 통계 기법
![](https://t1.daumcdn.net/cfile/tistory/99F325485C7B76BC2B)

### 3. 로지스틱 함수
* = 시그모이드(sigmoid) 함수
* 𝑥 데이터가 주어졌을 때 확률을 예측하는 로지스틱 회귀분석은 학습 데이터를 잘 설명하는 선형 판별식의 기울기 𝑎 와 절편 𝑏 을 찾는 문제
* 선형 판별식 값이 커지면 1, 작아지면 0에 가까운 확률값
* 기본적으로 임계값을 0.5로 함
    * 크면 1로 분류
    * 아니면 0으로 분류
    * 임계값은 사용자가 설정 가능

### 4. predic_proba
* 예측 단계에서 0, 1의 결과를 모델이 도출할 때, 0과 1이라는 결과가 어떻게 도출되었는지 각각의 확률값 출력
* `y_pred = model.predict_proba(x_test)`
* 결과 [[0.7, 0.3], [0.8, 0.2], [0.3, 0.7]]
    * 이 경우 첫번째는 0, 두번째는 0, 세번째는 1로 예측됨을 알 수 있다.