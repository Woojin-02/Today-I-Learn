# Random Search, Grid Search

* KNN 알고리즘이나 Decision Tree의 경우 하이퍼파라미터(n_neibors, max_depth 등) 존재
* 최선의 하이퍼파라미터 값 설정이 필요

방법 1. 1~n까지의 하이퍼파라미터 값을 모두 실행 후 가장 성능이 좋았던 하이퍼파리미터 값 찾기</br>
방법 2. 1~n까지의 하이퍼파라미터 값 중 랜덤하게 m개를 골라서, 가장 성능이 좋았던 하이퍼파리미터 값 찾기

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
```

### 1. Grid Search
* 방법 1
* 딕셔너리 형태로 파라미터 값 범위 지정
* 파라미터 값 범위를 모두 사용하는 Grid Search 모델 선언 후 학습
* 가장 좋은 성능을 보인 파라미터 값으로 자동 학습
* 모든 경우의 수를 확인하기 때문에 시간이 오래 걸림

### 2. Random Search
* 방법 2
* 딕셔너리 형태로 파라미터 값 범위 지정
* 파라미터 값 범위에서 몇개 선택할지 정하고 Random Search 모델 선언 후 학습
* 가장 좋은 성능을 보인 파라미터 값으로 자동 학습
* Grid_search 방법에서 n_iter 옵션 추가됨
* 일정한 개수를 뽑아서 진행하기 때문에 시간은 비교적 짧게 걸리나 랜덤으로 선택되지 않은 하이퍼파리미터값이 더 우수할 가능성을 배제하지 못함

### 3. 문법
```python
# 함수 불러오기
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV

# 파라미터 선언
params = {'max_depth':range(1, 31)}  # 30개 선언

# 기본 모델 선언
dt_model = DecisionTreeRegressor(random_state=1)

# Random Search 선언
  # cv=5
  # n_iter=20 / Grid Search 일 경우에는 n_iter만 빼고 나머지 그대로 사용
  # scoring='r2'
model = RandomizedSearchCV(dt_model,     # 기본 모델
                          params,        # 파라미터 범위
                          cv = 5,        # K-Fold 개수
                          n_iter = 20,   # 랜덤하게 선택할 파라미터(조합) 개수)
                          scoring='r2'   # 평가지표
                          )

# 모델 학습
model.fit(x_train, y_train)

# 결과 확인
print(model.cv_results_['mean_test_score'])  # 수행 정보 중 평균 성능값들 출력
print('최적파라미터:', model.best_params_)    # 최적 파라미터
print('최고성능:', model.best_score_)         # 최고성능

# 변수 중요도 확인
# model.best_estimator_.feature_importances_
# feature_importances_는 Decision Tree에만 있는 기능임
# model.feature_importances_를 사용하면 model이 Random 혹은 Grid Search를 가리키기 때문에 오류
# model.best_estimator_는 최선의 파라미터로 무장된 DecisionTree를 의미함
plt.barh(y=list(x), width=model.best_estimator_.feature_importances_)
```

### 4. K분할교차검증과의 차이
K분할교차검증은 하이퍼파라미터값을 하나로 고정하고,<br>
x_train 데이터를 k개로 나눠서 한번씩 평가, k-1개씩 학습한다<br>

RandomSearchCV는 하이퍼파라미터 값을 바꿔서(범위를 설정하고 그 범위 안에서 n_iter 만큼 랜덤 추출)<br>
K분할교차검증을 진행하고, 그중 가장 좋은 K분할교차검증이 나온 하이퍼파라미터와 그 값을 출력한다.<br>

### 5. Random Search + Grid Search
* Random Search와 Grid Search 사용 방법 중 하나
* Random Search로 무작위 수행된 뒤 도출된 최적값 선정 후에
* 선정된 최적값을 중앙값으로 두고 앞 뒤 범위를 지정해서 Grid Search 수행
* 그 결과 도출된 최적값을 최종 선정
    * 필요하다면 Grid Search를 여러번 진행할 수 있음
    * 첫번째 Grid Search 실행 시 설정한 범위의 끄트머리 파라미터가 선정되었을 경우 그 값을 중앙값에 두고 다시 실행

### 6. 주의사항
    학습데이터 기준으로 최적화된 데이터라고 실제 데이터와 예측값을 비교하면 성능이 떨어질 수 있음<br>
    과적합 될 수 있음<br>
    과하지도 부족하지도 않은 적절한 복잡도 필요
