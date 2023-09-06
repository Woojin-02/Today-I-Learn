# fit 함수 동작

### fit 함수를 사용했을 때
```python
# fit 함수를 사용했을 때
# 모델 준비
X = tf.keras.Input(shape=[13])
H = tf.keras.layers.Dense(128, activation='swish')(X)
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.Model(X, Y)
model.compile(loss='mse')

model.summary()

# 모델 학습
model.fit(독립, 종속, epochs=1000)

# 모델 사용
model.predict(독립)
```

### model.fit() 풀어쓰기
```python
# fit 함수를 사용했을 때
# 모델 준비
X = tf.keras.Input(shape=[13])
H = tf.keras.layers.Dense(16, activation="swish")(X)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Dense(16, activation="swish")(H)
H = tf.keras.layers.BatchNormalization()(H)
Y = tf.keras.layers.Dense(1)(H)
model = tf.keras.Model(X, Y)
model.compile(loss='mse', optimizer='adam')

model.summary()

# 모델 학습
# 수동으로 fit 실행(pyTorch에서는 이런 식으로 학습 실행)
loss = tf.keras.losses.MeanSquaredError()    # 손실함수
optim = tf.keras.optimizers.Adam(learning_rate=0.001)     # 최적화 함수
# learning_rate랑 워크북 파일의 dt값과 다름 / running rate는 다음 값을 정하는 nextW의 수식

for e in range(1000):       # 학습 횟수(epochs=1000)
    with tf.GradientTape() as tape :
        pred = model(독립.values, training=True)    # 예측값
        cost = loss(종속, pred)                     # 정답과 예측값을 이용해서 cost(오차)를 구함
    # cost를 작게 만들기 위해 weight를 조정해야 하는데, 그게 바로 아래의 2줄
    grad = tape.gradient(cost, model.trainable_variables) # W가 들어올 때마다 cost가 어떻게 변하는지 각각의 미분값을 구해라
    optim.apply_gradients(zip(grad, model.trainable_variables)) # W1에 대한 미분값을 구하고 적용함
    print(e, cost)
```
