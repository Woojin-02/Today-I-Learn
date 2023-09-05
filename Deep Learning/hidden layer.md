# hidden layer

* 머신러닝에서 유의미한 변수를 찾는 작업은 중요함
* 이 작업은 데이터 엔지니어가 함(feature Engineering)
* 딥러닝은 이 작업을 스스로 할 수 있음

### 1. 특징 자동 추출기
* 딥러닝은 스스로 최종 결과 도출에 도움이 되는 변수를 뽑음
* 사람은 특징을 몇개까지 뽑을지만 결정함
* 이 특징 때문에 특징 자동 추출기라고 부름
* 입력된 모든 x변수를 이용해서 새로운, 유의미한 h 변수 생성. 즉, x와 h는 다른 변수임
* 생성된 h를 이용해서 최종 결론인 y를 예측함

```python
X = tf.keras.Input(shape=[13])
H = tf.keras.layers.Dense(128, activation='swish')(X) # 13개의 변수에서 128개의 새로운 hidden layer 생성
H = tf.keras.layers.Dense(64, activation='swish')(H) # H를 이용해서 또 새로운 H 생성 가능
Y = tf.keras.layers.Dense(1)(H)
model = tf.keras.Model(X, Y)
model.compile(loss='mse')
```

### 2. hidden의 특징
* hidden을 만든다는 것 : 
    * x가 10개고 히든을 5개 만들려고 할 때, 10차원에 있는 변수의 개수를 5차원의 공간으로 변환하는 작업임
* 분류 문제일 경우 다른 차원의 공간으로 변환된 데이터들의 위치가 서로 모여 있으면, 유의미한 변환임
* 회귀 문제일 경우 다른 차원의 공간으로 변환된 데이터들의 위치가 선형성을 띄면, 유의미한 변환임