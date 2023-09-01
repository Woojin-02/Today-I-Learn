# Hyperparameter

* 알고리즘을 사용해 모델링할 때 모델 성능을 최적화하기 위해 조절할 수 있는 매개변수
* 최선의 하이퍼파라미터 값을 찾기 위해 튜닝해야 함
* Grid Search, Random Search 등 방법이 있음

### 1. KNN의 Hyperparameter
1. `n_neighbors=`
* KNN은 k값에 따라 성능이 달라짐
* k값은 클수록 단순하고 작을 수록 복잡함
* 테스트 데이터 반경 k개의 평균, 혹은 최빈값을 구함

2. 거리 계산법
* 유클리드 거리
* 맨하튼 거리

### 2. Decision Tree의 Hyperparameter
1. max_depth
* 트리의 최대 깊이 제한
* 값이 작을수록 트리 깊이가 제한되어 모델이 단순헤짐

2. min_samples_leaf
* leaf가 되기 위한 최소한의 샘플 데이터 수
* 이 값이 클수록 모델이 단순해짐

3. min_samples_split
* 노드를 분할하기 위한 최소한의 샘플 데이터 수
* 이 값이 클수록 모델이 단순해짐

4. 예시
* min_samples_split= 30 , min_samples_leaf = 10
    * 노드의 데이터 개수가 30개라면, [5, 30]으로 나누기 불가, [10, 25]로는 분기 가능
    * 노드의 데이터 개수가 25개 일때, [10, 15]라도 분기 불가. 개수가 30개 이상이어야 함