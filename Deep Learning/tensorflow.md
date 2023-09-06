# tensorflow

### 1. 데이터 준비

```python
# 데이터 준비
import tensorflow as tf
import pandas as pd

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# 표로 만들기
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# 정답데이터 원핫인코딩
y_train = pd.get_dummies(y_train)
y_test = pd.get_dummies(y_test)

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)
```

* 원래 (60000, 28, 28) 크기의 데이터를 reshape를 통해 표(dataframe) 모양으로 만드는 과정이 필요하다.
* 또한 정답데이터가 0~9 인 범주형이므로 get_dummies를 이용해 원핫인코딩을 진행해야 한다.

```python
import tensorflow as tf

# cifar10
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Normalize(선택사항)
x_train = x_train / 255.
x_test = x_test / 255.
```
* 후의 모델 생성 과정에서 어떻게 하느냐에 따라 reshape 과정을 생략할 수 있다.
    * H = tf.keras.layers.Flatten()(X)를 모델 준비 과정에 삽입하면 reshape를 하지 않아도 된다.

* 범주형 데이터의 값에 따라 원핫 인코딩을 생략할 수 있다.
    * 숫자 레이블링이 끝나 있는 분류 상태일 경우
    * 클래스가 4개 있을 때, 그 값이 0, 1, 2, 3인 경우에만. 값이 setosa, versinica 이런거면 안되고 오로지 0, 1, 2, 3, ...인 경우에만 가능
    * 모델 준비 단계에서의 메커니즘은 원핫인코딩을 한 것과 똑같이 해야함
        * 현재 정답데이터의 열 개수는 1이지만, 원핫인코딩을 하면 10개로 나뉘기 때문에 Dense에 10을 줘야 한다.
        * 또한 sparse_categorical_crossentropy를 사용해야 한다.
        * Y = tf.keras.layers.Dense(**10**, activation="softmax")(H)
        * model.compile(loss="**sparse_categorical_crossentropy**", metrics="accuracy")


### 2. 모델 생성

```python
X = tf.keras.Input(shape=[32, 32, 3]) # reshape 생략 / 생략하지 않았을 경우엔 3072 입력
H = tf.keras.layers.Flatten()(X)  # reshape 생략

H = tf.keras.layers.Dense(1024)(H) # Dense의 값이 크면 잘 되는 것 같음
H = tf.keras.layers.BatchNormalization()(H) # BatchNormalization은 swish 전에 진행해야 함
H = tf.keras.layers.Activation('swish')(H)

for i in range(16):
    H1 = tf.keras.layers.Dropout(0.5)(H) # Dropout
    H1 = tf.keras.layers.Dense(1024)(H1)
    H1 = tf.keras.layers.BatchNormalization()(H1)
    H1 = tf.keras.layers.Activation('swish')(H1)

    H1 = tf.keras.layers.Dense(1024)(H1)
    H1 = tf.keras.layers.BatchNormalization()(H1)
    H = tf.keras.layers.Add()([H, H1]) # skip connection
    H = tf.keras.layers.Activation('swish')(H)

Y = tf.keras.layers.Dense(10, activation=tf.keras.activations.softmax)(H) # 문자열 입력 부분 함수로 대체 가능
model = tf.keras.Model(X, Y)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), # optimizer 선택
              loss="sparse_categorical_crossentropy",
              metrics="accuracy"
)
model.summary()
```

1. BatchNormalization
* Overfitting 방지의 한 방법
* 실제로는 Overfitting에는 별 효과 없음. Underfitting에는 효과적
* Layer 사이의 스케일을 맞춤
* swish, ReLU 등은 음수를 모두 0으로 처리하기 때문에 BatchNormalization를 한 후에 swish를 하는 것이 기본
* 무조건 사용한다.

2. Dropout
* 데이터의 일정 비율을 0으로 만든다.
* 노드를 랜덤하게 제거하면, 사실상 각각 다른 모델이 되기 때문에 앙상블처럼 여러개의 모델로 학습하는 효과가 있다.
* 즉 Overfitting을 해결할 수 있다.
* Dense값이 16, 10 정도로 낮으면 0.20 정도만 삭제해야 하지만,
* Dense값이 크면 0.50, 0.60으로 40~50%만 학습해도 충분한 성과가 나온다. 오히려 0.5, 0.6을 권장.

3. skip connection
* 깊은 망
* layer 수가 엄청나게 증가하면 성능이 급격히 향상되는 것을 보고, layer끼리 연결시키기로 함
* skip connection을 쓰지 않고서는 히든레이어를 100개 이상으로 쌓을 수 없음
* skip connection을 걸려면 hidden layer Dense 값을 다 통일해야 함
* 반복문을 사용하면 구현하기 더 쉬움
    * skip connection을 사용하지 않을 때 코드 예시

```python
X = tf.keras.Input(shape=[32, 32, 3])
H = tf.keras.layers.Flatten()(X)

H = tf.keras.layers.Dropout(0.5)(H)
H = tf.keras.layers.Dense(1024)(H)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Activation('swish')(H)

H = tf.keras.layers.Dropout(0.5)(H)
H = tf.keras.layers.Dense(1024)(H)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Activation('swish')(H)

H = tf.keras.layers.Dropout(0.2)(H)
Y = tf.keras.layers.Dense(10, "softmax")(H)
model = tf.keras.Model(X, Y)
model.compile(loss="sparse_categorical_crossentropy", metrics="accuracy", optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001))
model.summary()
```

4. 문자열 입력 부분을 함수로 대체

```python
X = tf.keras.Input(shape=[784])
H = tf.keras.layers.Dense(120, activation='swish')(X) # tf.keras.activations.swish
H = tf.keras.layers.Dense(84, activation='swish')(H) # tf.keras.activations.swish
Y = tf.keras.layers.Dense(10, activation='softmax')(H) # tf.keras.activations.softmax
model = tf.keras.Model(X, Y)
model.compile(
                loss='categorical_crossentropy', # tf.keras.losses.categorical_crossentropy
                optimizer='adam' # tf.keras.optimizers.Adam(learning_rate=0.0001)
                metrics='accuracy' # tf.keras.metrics.sparse_categorical_accuracy
)
```

### 3. 모델 학습

```python
# 모델 학습
early = tf.keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True) # Early Stopping
result = model.fit(x_train, y_train, epochs=50, batch_size=128,
                   validation_split=0.2, # validation
                   callbacks=[early] # callback
)
```

1. validation(검증)
* validation은 학습 도중에 overfitting을 모니터링하기 위한 데이터 셋
* 테스트 데이터로 평가하기 전에 모델의 정확도를 확인하기 위해서 사용하거나
* 학습 도중에 오버피팅(과적합)이 발생했는지 확인하기 위해서 사용
    * 학습 시간이 오래 걸리기 때문에, 그 중간에 잘 학습되고 있는지 확인할 수 있는 방법이 필요했음
* loss는 줄어드는데 val의 loss 늘어나면 오버피팅되는 것
* 학습 한 번 진행 완료하고 -> validation 진행 -> 학습 두 번째 진행 완료하고 -> validation 진행 -> ... 이 순서로 validation이 진행
    * 즉, epochs 값만큼 validation이 진행

    결과 예시<br>
    loss: 0.0353 - accuracy: 0.9913 - val_loss: 0.6346 - val_accuracy: 0.9607

* `validation_split=0.2`는 기존 데이터셋의 마지막 20% 가량을 validation 용으로 사용하겠다는 의미
* validation 데이터가 따로 존재하는 경우에는 `validation_data=(x_val, y_val)` 사용

2. callbacks
* fit 함수가 끝날때마다(=epochs가 끝날때마다) callback함
* 데이터를 저장하거나, learning rate를 저정하거나 등 다양한 활동이 가능함

3. Early Stopping
* callback의 일부
* overfitting이 발생하면 멈추고 멈추기 전 최적의 모델을 적용한다.
```python
early = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', # val_loss를 기준으로 작동
    min_delta=0,  # 이 보다 작게 변하면 변한다고 안할거임.
    patience=10,  # 이 횟수(epoch) 동안 개선이 없으면 끝냄.
    restore_best_weights=True # 멈추기 전 최적의 모델을 적용
)

```

#### 번외
```python
result.history
```
* 학습진행 log 확인가능
* loss와 metrics으로 지정된 값이 로깅됨
* 시각화 가능
```python
import matplotlib.pyplot as plt
plt.plot(result.history['loss'])
plt.plot(result.history['val_loss'])
plt.legend(['loss', 'val_loss'])
plt.show()
```

### 4. 모델 평가

```python
# 모델 평가
model.evaluate(x_test, y_test)
# 출력 loss: 1.6037 - accuracy: 0.4820
```
* 최종 테스트 값