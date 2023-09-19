# CNN과 Object Detection

1. Feature Representation
 * 모델을 학습할 때, 각 노드들은 연결된 것으로부터 기존에 없던 새로운 Feature를 추출한다.
    * 이때, 성능상으로 유양하다고는 할 수 있지만, 설명을 통해 모델이 유용하다고 입증하기는 어렵다.
    * 모델의 각 Feature가 어떻게 생성되는지 모르기 때문이다.

2. CNN에서의 Feature Representation
 * CNN에서는 위치 정보를 보존한다.
 * 즉, CNN에서의 Feature Representation은 CNN을 통해 보존된 위치정보를 포함하여 Feature를 만들어낸다.
    * 이때 만들어지는 Feature에 위치정보가 활용되는지는 알 수 없다. 다만 이렇게 했더니 성능이 올라갔기 때문에 이 방법을 사용한다.

3. CNN과 Object Detection의 관계
* CNN에서 Feature Representation을 할 때, 목적에 따라 어떤 Feature를 추출하는지가 달라진다.
* 즉, CNN은 그대로 진행하고, flatten 이후의 feature 추출에서 어떤 feature를 추출하는지를 바꿀 수 있다.
* 다시 말해서 *대회에 사용된 CNN 모델의 구조와 가중치 + 우리 문제에 필요한 구조*를 덧붙일 수 있다.
* Object Detection 역시 우리 문제에 필요한 구조를 CNN 모델의 구조와 가중치에 덧붙인 것의 일환이다.
* 이때 대회에 사용된 CNN 모델의 구조와 가중치는 `backbone`이라고 하고,
* 우리 문제에 필요한 구조는 `head`라고 한다.
    * 최근에는 `neck`이라고, backbone과 head 사이를 좀 더 잘 연결되게 해주는 것도 추가되었다.