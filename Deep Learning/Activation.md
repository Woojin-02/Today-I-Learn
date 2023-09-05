# Activation (활성화 함수)

* Sigmoid, tanh, ReLU, Leaky ReLU, Maxout, ELU 등 다양한 함수가 있음
* vanishing gradient는 sigmoid, tanh를 사용하면서 발생함
    * 미분값이 0에 수렴하게 되면서 맨 앞쪽 레이어의 weight의 변화가 loss에 영향을 주지 못했기 때문에, weight를 조정할 수 없어서 발생함
* 최근의 활성화 함수
    * swish
    * GELU