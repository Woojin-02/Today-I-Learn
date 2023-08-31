# K-Fold Cross Validation

* K 분할 교차 검증
* 이름에도 나오듯 모델 평가를 위한 함수

```python
from sklearn.model_selection import cross_val_score
```

### 1. 개념
* 모든 데이터가 평가에 한번, 학습에 k-1번 사용됨
* 데이터를 k개로 분할한 후, 나머지 데이터로 성능을 예측함 -> k번만큼 반복
* 반복한 값의 평균과 표준편차를 계산하면, 해당 알고리즘을 사용한 모델의 성능의 일반화가 가능
* 단, k는 2 이상이 되어야 함
    * 최소한 한개의 학습용, 한개의 검증용 데이터가 필요하기 때문
* 모델의 성능이 좋아지는 것이 아니라 이 모델의 평균 성능이 어떤지 확인
* 실제 평가에서 얻은 성능이 이 성능보다 더 높거나 낮을 수 있음

![](https://jinnyjinny.github.io/assets/post_img/deep%20learning/2020-04-02-Kfold/main1.png)

### 2. 장단점

1. 장점
* 모든 데이터를 학습과 평가에 사용할 수 있음
* 데이터가 부족해서 발생하는 과소적합 문제를 방지
* 평가에 사용되는 데이터의 편향 방지
* 정확도 향상
* **일반화된 모델 생성 가능**

2. 단점
* 반복 횟수가 많아서 모델 학습과 평가에 많은 시간이 소요됨

### 3. 예시 코드 및 시각화

1. 분류의 경우
```python
# 불러오기
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# 선언하기
model1 = KNeighborsClassifier(n_neighbors=5)
model2 = DecisionTreeClassifier(random_state=1)
model3 = LogisticRegression()

# 검증하기
cv_score1 = cross_val_score(model1, x_train_s, y_train, cv=5) # x_train_s : scaling 진행한 x_train 데이터
cv_score2 = cross_val_score(model2, x_train, y_train, cv=5)# cv : k값 설정
cv_score3 = cross_val_score(model3, x_train, y_train, cv=5)

# 확인
print(cv_score1, cv_score2, cv_score3)
print("평균:", cv_score1.mean(), cv_score2.mean(),cv_score3.mean())
print("표준편차:", cv_score1.std(), cv_score2.mean(),cv_score3.mean())
```

2. 시각화
```python
# 딕셔너리에 저장
result = {}
result['KNN'] = cv_score1.mean()
result['DecisionTree'] = cv_score2.mean()
result['LogisticRegression'] = cv_score3.mean()

# 시각화
plt.barh(y=list(result), width=result.values())
plt.show()
```