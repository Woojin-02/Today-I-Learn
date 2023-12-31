# GAN

### 강화학습

어떤 환경 안에서 정의된 에이전트가 현재의 상태를 인식하여, 선택 가능한 행동들 중 보상을 최대화하는 행동 혹은 행동 순서를 선택하는 방법

### GAN(Generative Adversarial Networks / 적대적 생성 신경망)

* 보통 생성형 AI 라고 부른다.
* 실제에 가까운 이미지나 사람이 쓴 것과 같은 글 등 여러 가짜 데이터들을 생성하는 모델
* 서로 다른 두 개의 네트워크를 적대적으로(adversarial) 학습시키며 실제 데이터와 비슷한 데이터를 생성(generative)해내는 모델
* label이 없기 때문에 비지도학습 기반 모델


**1. GAN의 원리**

* 실제처럼 보이는 데이터를 생성하는 Generator / 데이터를 구별하는 판별모델 discriminator
* 생성 모델은 끊임없이 거짓 예제를 만들어내고, 상대는 실제 데이터와 만들어진 가짜 데이터를 구별하는 것으로 학습한다.
    * 위조지폐범은 계속해서 정교한 위조지폐를 만들어내려고 하고, 경찰은 계속해서 위조지폐를 판별해내는 것과 같은 원리다.
* 최종적으로 Generator가 실제 데이터와 비슷한 것을 생성하는 Generative Model이 되는 것을 목표로 한다.
* 어느 순간부터 Generator는 가장 완벽한 가짜 데이터를 만들 수 있게 되고, 그러면 discriminator는 결국 해당 데이터의 참과 거짓을 구분할 수 없다.
* 확률이 50%에 수렴하면 학습이 종료된다.

**2. GAN의 특징**
* GAN을 이용하면 loss를 사용자가 원하는 것으로 커스터마이징 할 수 있다.