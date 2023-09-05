# hidden layer

* 머신러닝에서 유의미한 변수를 찾는 작업은 중요함
* 이 작업은 데이터 엔지니어가 함(feature Engineering)
* 딥러닝은 이 작업을 스스로 할 수 있음

### 1. 특징 자동 추출기
* 딥러닝은 스스로 최종 결과 도출에 도움이 되는 특징을 뽑음
* n개의 독립변수가 있을 때, 독립변수를 이용해서 m개의 새로운 특징을 만들어냄. 어떤 경위로 특징이 생성되는지는 알 수 없음
* 사람은 특징을 몇 개 뽑을지만 결정함
* 이 특징 때문에 특징 자동 추출기라고 부름
* 입력된 모든 x변수를 이용해서 새로운, 유의미한 h 변수 생성. 즉, x와 h는 다른 변수임
* 생성된 h를 이용해서 최종 결론인 y를 예측함
* feature를 5차원 공간으로 이동시켜 새로운 feature를 만들어냄
    * 공간으로 이동시키면 각 feature간의 거리를 알 수 있음. classification(분류)의 경우 거리가 멀면 서로 관련이 없고, 거리가 가까우면 서로 관련이 있음. 서로 쉽게 분리가 되는 분포를 형성한다면, 분류하는데에 더 유리함
    * 또한 수식으로 만들어내기 때문에 입력한 feature의 개수보다도 더 많은 특징을 만들어낼 수 있

```python
X = tf.keras.Input(shape=[13])
H = tf.keras.layers.Dense(128, activation='swish')(X) # 13개의 변수에서 128개의 새로운 hidden layer 생성
H = tf.keras.layers.Dense(64, activation='swish')(H) # H를 이용해서 또 새로운 H 생성 가능
Y = tf.keras.layers.Dense(1)(H)
model = tf.keras.Model(X, Y)
model.compile(loss='mse')
```

### 1. 히든레이어의 개수
* 학습이 잘 안됨 -> 차원을 늘려야 함
* 학습이 너무 과함 -> 차원을 줄여야 함
* 차원 : H = tf.keras.layers.Dense(**64**, activation='swish')(H)에서 숫자 '64' 부분
* 보통 데이터가 많으면 128->64->32->... 으로 점점 차원을 줄이면서 학습한다.
