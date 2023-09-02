# 앙상블(Ensemble)

* 여러개의 모델을 결합하여 훨씬 강력한 모델 생성
* 성능이 좋지만 설명하기 힘들다는 단점이 존재
* 캐글(Kaggle) 같은 기계학습 경쟁에서 많이 사용됨
* 방법 : 보팅(Voting), 배깅(Bagging), 부스팅(Boosting), 스태킹(Stacking)

### 1. Voting
* 여러 모델들의 예측 결과를 투표하고, 이를 통해 최종 예측 결과 결정
    * EX) 한 Data Set을 Deicision Tree, K Nearest Neighbor, Logistic Regression으로 예측한 후 투표
* 하드 보팅
    * 최종값=다수의 모델이 예측한 값(다수결)
* 소프트 보팅
    * 모든 모델이 예측한 값이 결정되게 한 확률값의 평균을 구한뒤 가장 높은 확률을 채택

### 2. Bagging
* Bootstrap Aggregating
* 약간은 중복이 된 서로 다른 데이터를 가지고 같은 유형의 알고리즘 기반 모델을 사용함
    * 데이터 분할 시 중복을 허용함 => 복원 랜덤 샘플링 방식
    * 부트스트랩(복원추출)한 데이터로 모델들을 학습시키고, 모델들의 예측 결과를 집계해 최종 결정함
* 범주형 데이터 : 투표 방식으로 집계
* 연속형 데이터 : 평균으로 결과 집계
* 예시 : Random Forest

#### RandomForest
* Bagging의 가장 대표적인 알고리즘
* 여러 Decision Tree 모델이 전체 데이터에서 랜덤하게 데이터를 추출하고, 각자 데이터 샘플링을 함
    * 이때 랜덤하게 데이터를 샘플링할 때(복원 랜덤 샘플링 방식),
    * Decision Tree의 분할 기준이 되는 Feature를 랜덤으로 선택함.
* 모델들이 개별적으로 학습을 수행한 뒤 모든 결과를 집계햐여 최종 결과 결정
* 하이퍼파라미터

```python
from sklearn.ensemble import RandomForestClassifier
```

|파라미터|설명|
|:---:|:---:|
|**n_estimators**|만들어질 Decision Tree 개수(기본값 100)|
|max_depth|트리의 최대 깊이(기본값 None)|
|min_samples_split|노드를 분할 하기 위한 최소 샘플의 개수(기본값 2)|
|min_samples_leaf|트리가 분기해서 리프 노드를 만들려고 할 때, 만들어지는 리프 노드가 가질 수 있는 샘플 수|
|max_feature|데이터 학습 시 feature 수 제한. 이때, 랜덤하게 feature 추출|

### 3. Boosting
* 같은 유형의 알고리즘 기반 모델 여러개로 순차적으로 학습
* 이전 모델이 제대로 예측하지 못한 데이터에 가중치를 부여하여, 다음 모델이 수행할 y값으로 설정하고 학습과 예측을 진행
* 성능이 좋지만, 속도가 느리고 과적합 발생 가능성이 있음
* 예시 : XGBoost, LightGBM

#### XGBoost
별도의 install 필요
```python
!pip install xgboost
!pip install lightgbm

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
```

* 회귀, 분류 모두 지원
* 높은 예측 성능
* 빠른 수행시간(그러나 다른 알고리즘에 비하면 느림)
* 과적합 규제 기능
* 하이퍼퍼라미터로 가지치기 가증
* 학습 데이터와 검증 데이터에 대한 교차 검증을 수행
* 결측치 자체 처리

|파라미터|설명|
|:---:|:---:|
|**n_estimators**|실행되는 알고리즘 개수(기본값 100)|
|max_depth|트리의 최대 깊이(기본값 None)|
|learning_rate||
|min_child_weight||
|gamma||
|sub_sample||
|colsample_bytree||
|reg_lambda||
|reg_alpha||

### 4. Stacking
* 여러 모델의 예측 값을 최종 모델의 학습데이터로 사용함
* KNN, Logistic Regression, XGBoostXGBoost모델을 사용해 4종류 예측값을 구한 후
* 이 예측 값을 최종 모델인 Randomforest 학습 데이터로 사용
* 현실에선 많이 사용되지 않지만, 미세한 성능 차이로 승부를 결정짓는 대회에선 사용됨
* 기본 모델로 4개 이상 선택해야 좋은 결과를 기대할 수 있음
