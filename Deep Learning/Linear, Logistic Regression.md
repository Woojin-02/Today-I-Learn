# Linear Regression, Logistic Regression

### 1. 선형회귀와 최소제곱추정
* sum of loss = (실제값 - 예측값)^2의 합
* sum of loss가 최소가 되도록 예측값에 있는 w, b값을 조정하여, loss 값이 최소가 되는 수식을 찾아내면 그것이 모델이 됨
* 코드
```python
X = tf.keras.layers.Input(shape=[13])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse', optimizer='adam')
```

### 2. 로지스틱 회귀와 크로스 엔트로피
* 시그모이드로 fitting해서 그래프를 그리면 -> 로지스틱 회귀
* 수식을 정리하면 : 
    * y가 0일때는 로스를 -log(1-y.hat), 1일때는 로스를 -log(y.hat)을 사용한다는 의미
    * 값을 올바르게 예측하면(0을 0으로, 1을 1로) log값이 0이 되고, 반대로 값을 틀리게 예측하면(0을 1로, 1을 0으로 예측) log값이 무한으로 수렴한다.
* 코드
```python
X = tf.keras.layers.Input(shape=[4])
Y = tf.keras.layers.Dense(1, activation='sigmoid')(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='binary_crossentropy',optimizer='adam')
```

### 3. 퍼셉트론(Perceptron)
* 뉴런과 비슷하게 동작함.
1. 신호들을 받아서
2. 신호들을 조합하고
3. 일정 기준치를 넘는지 확인한 후에(활성화 함수 사용)
4. 넘으면 output:1, 안넘으면 output:0
* 예전에는 sigmoid를 사용했기 때문에 제대로 동작하지 않음. ReLU 함수를 쓰면서 퍼셉트론을 사용할 수 있게 됨
