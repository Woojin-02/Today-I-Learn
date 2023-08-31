#  Decision Tree

* ***회귀, 분류 모델 모두 사용 가능***
* 설명하기 쉽다는 특징

```python
# 회귀 모델 구현
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 분류 모델 구현
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
```

### 1. Decision Tree
* 결정 트리, 의사 결정 나무
* 특정 변수에 대한 의사결정 규칙을 나무 가지가 뻗는 형태로 분류
* 스케일링 등의 전처리 영향도가 크지 않음. 오히려 가변수화 등은 방해됨
* 분석 과정을 실제 눈으로 확인할 수 있는 화이트박스 모델
* 의미있는 질문을 먼저 해서 분류하는 것이 중유
* 과적합이 일어나기 쉬움
* 가지치기(트리가 학습 데이터를 과하게 학습하지 않도록) 튜닝이 필요

### 2. Decision Tree 용어
* `Root Node` : 뿌리마디. 전체 자료를 갖고 시작하는 첫 마디.
* `Terminal Node(Leaf Node)` : 끝마디. 자식 마디가 없는 마디.
* `Depth` : 깊이. 아래로 연결된 마디와 마디 사이에 연결된 화살표 개수
* Child Node : 자식마디. 마디 하나로부터 분리된 마디.
* Parent Node : 부모 마디. 주어진 마디의 상위 마디.
* Internal Node : 중간 마디 : 부모 마디와 자식 마디가 모두 있는 마디.
* Branch : 가지. 연결되어 있는 2개 이상의 마디 집합.

### 3. 분류와 회귀
* 분류 : 마지막 노드에 있는 샘플들의 최빈값(class로 표현되는 값)을 반환
* 회귀 : 마지막 노드에 있는 샘플들의 평균을 예측값으로 반환

1. 분류문제
* 불순도와 순도
    * 순도가 높을수록 분류가 잘 됨
    * y의 값이 0, 1만 있는 이준 분류 기준으로 불순도 50%가 가장 불순도가 높음
    * 수치화 : 지니 불순도, 엔트로피
* 지니 불순도(Gini Impurity)
    * 1-(양성클래스비율의 제곱 + 음성클래스비율의 제곱)
    * 지니 불순도가 낮을수록 순도가 높음
    * 완벽하게 분류되면 0
    * 완벽하게 섞이면 0.5
* 엔트로피(Entropy)
    * 속성의 불순도만 표현
    * 완벽하게 분류되면 0
    * 완벽하게 섞이면 1

2. 회귀문제
* MSE

3. *정보 이득(Information Gain)*
* 정보 이득이 큼 = 해당 속성으로 분할할 때 불순도가 줄어듬
* 정보 이득이 가장 큰 속성부터 분할
* ``부모의 불순도 - 자식의 불순도``
    * 자식의 불순도가 작아진다는 뜻
* 변수들 중 2개 이상이 같은 정보 이득을 보이면, 랜덤하게 선택해서 시작힘

### 4. 가지치기
* Decision Tree는 아주 세밀하게 학습하도록 기본값이 설정되어있기 때문에 가지치기 필요
    * 모델이 학습데이터에는 매우 잘 맞지만, 평가데이터에는 잘 맞지 않는 과적합 방지
* 하이퍼파라미터 값 조정

|파라미터|설명|
|:---:|:---:|
|max_depth|트리의 최대 깊이(기본값 None)|
|min_samples_split|split할 수 있는 최소 샘플의 개수(기본값 2)|
|min_samples_leaf|트리가 분기해서 리프 노드를 만들려고 할 때, 만들어지는 리프 노드가 가질 수 있는 샘플 수(기본값 1)|
|max_feature|데이터 학습 시 feature 수 제한. 이때, 랜덤하게 feature 추출|
|max_leaf_node|리프 노드 최대 개수|

* 이중 `max_depth`, `min_samples_split`, `min_samples_leaf`는 중요
* max_depth
    * 보통 max_depth만 제한함
    * 적당히 깊이 분할하도록 조정
* min_samples_split
    * split할 수 있는 최소 샘플의 개수
    * 값을 2로 설정하면 완벽히 분할되지 않은 값이 2개 있으면 그걸 또 나눔 = 엄청 세밀하게 분할됨
    * 값을 10으로 설정하면 완벽히 분할되지 않은 값이 있어도 그 개수가 10개 이상이어야만 분할함
* min_samples_leaf
    * 트리가 분기해서 리프 노드를 만들려고 할 때, 만들어지는 리프 노드가 가지고 있는 샘플 수
    * 만약 기본값이 10이면, 부모 노드의 샘플 수가 10 이하면 자식(리프노드)의 샘플 수는 절대로 10을 넘을 수 없기 때문에 리프노드가 만들어지지 않음

### 5. 변수 중요도
* `model.feature_importances_`

### 6. 시각화
#### 1. graphviz로 시각화
    * 관련 라이브러리를 따로 크롬이나 웨일 등에서 다운로드 및 설치해야함
    * plot_tree보다 가독성 있는 시각화 가능

```python
# 시각화 모듈 불러오기
from sklearn.tree import export_graphviz
from IPython.display import Image

# 이미지 파일 만들기
export_graphviz(model,                                 # 모델 이름
                out_file='tree.dot',                   # 파일 이름
                feature_names=x.columns,               # Feature 이름 / list(x)도 같은 결과
                class_names=['Woman', 'Man'],          # Target Class 이름 / 반드시 문자열을 입력
                rounded=True,                          # 둥근 테두리
                precision=2,                           # 불순도 소숫점 자리수
                max_depth=3,                           # 3단계만 표시
                filled=True)                           # 박스 내부 색깔 채우기. 진할수록 순도 높음

# 파일 변환
!dot tree.dot -Tpng -otree.png -Gdpi=300

# 이미지 파일 저장
Image(filename='tree.png')
```

* 주의 !class_names!
    * 타겟 값(0, 1)이 아니라 그 클래스를 설명할 수 있는 단어(문자열)을 기입해야 함
    * ***원래 데이터에서 알파벳 순으로 정렬되어 시각화, 라벨은 본인이 보고 싶은 이름을 부여***
        * 그래프의 value 값은 알파벳 순으로 나옴
        * value 값을 설명하기 위해 쓰는 class_names은 target의 value값이 어떤 것을 의미하는지 설명함
        * 따라서 더 앞선 알파벳인 target의 value를 가리키는 라벨을 부여하고 싶으면, 앞에 해당 라벨을 붙여야함
        * Sex target의 값인 0의 뜻이 female, 1의 뜻이 일 때 Woman, Man으로 class_names 표현하고 싶으면
        * class_names = ['Woman', 'Man']이어야 함
        * Sex target의 값이 female, male 두가지가 있고, Female, Male로 class_names를 추가하고 싶으면
        * class_names = ['Femal', 'Male']
            * target의 두 값 중 female이 먼저 나오기 때문에 데이터의 순서는 무조건 female, male로 고정됨
            * 따라서 라벨링도 Famale, Male 순서로 입력

#### 2. 변수 중요도 시각화
* feature_importances_ 속성 값으로 변수 중요도 확인
* 현재 생성된 Decision Tree 입장에서 변수의 중요도를 보여줌.
    * 즉, 변수의 중요도를 보여주기 위해 Decision Tree를 사용할 필요는 없지만, Decision Tree를 사용했다면 feature_importances_를 확인해야함
* 값이 클수록 Feature의 중요도가 높음