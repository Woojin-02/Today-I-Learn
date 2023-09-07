# ## class model Code

* input 데이터의 shape를 자동으로 잡음. input 데이터의 shape를 굳이 확인하지 않아도 된다는 장점이 있음
* 원래 함수를 커스터마이징하여 사용
* 커스터마이징하여 많이 사용함

1. 클래스 생성
```python
# class 생성
# GradintTape
import tensorflow as tf

# Mnist Fashion 데이터 모델 준비하는 클래스
class MyFashionMNISTModel(tf.keras.Model):
    def __init__(self, **kwargs):
        super(MyFashionMNISTModel, self).__init__(**kwargs)
        self.flatten = tf.keras.layers.Flatten()
        self.dense1 = tf.keras.layers.Dense(64, activation="swish")
        self.bn1 = tf.keras.layers.BatchNormalization()
        self.dense2 = tf.keras.layers.Dense(64, activation="swish")
        self.bn2 = tf.keras.layers.BatchNormalization()
        self.dense3 = tf.keras.layers.Dense(10, activation="softmax")
        # self.compile()

    #  tf.keras.layers.Add()를 통해 skip connection을 하려는 경우 따로 반복문 함수를 만들어야 한다.

    def call(self, X):
        H = self.flatten(X)
        H = self.dense1(H)
        H = self.bn1(H)
        H = self.dense2(H)
        H = self.bn2(H)
        Y = self.dense3(H)
        return Y
    # 한번 돌리면 가중치가 생기기 때문에 할때마다 새로운 bn, dense를 써야 한다. layer나 activation layer도 만든다고 하면 따로 만들어야 함

    # fit을 실행하면 train_step이 실행됨
    # batch는 일반적으로 모델을 학습할 때 데이터로부터 생성됨
    def train_step(self, batch):
        x_batch, y_batch = batch

        with tf.GradientTape() as tape:
            y_pred = self(x_batch, training=True)
            loss = self.compiled_loss(y_batch, y_pred)

        grad = tape.gradient(loss, self.trainable_weights)
        self.optimizer.apply_gradients(zip(grad, self.trainable_weights))

        self.compiled_metrics.update_state(y_batch, y_pred)
        return {m.name: m.result() for m in self.metrics}

    # test
    def test_step(self, batch):
        x_batch, y_batch = batch
        y_pred = self(x_batch, training=True)

        self.compiled_loss(y_batch, y_pred)
        self.compiled_metrics.update_state(y_batch, y_pred)

        return {m.name: m.result() for m in self.metrics}

model = MyFashionMNISTModel()
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics="accuracy")
# compile을 추가하지 않으면 동작하지 않는다.
model.build(input_shape=[None, 28, 28]) 
# model.build로 input_shape[28, 28]를 넣어야 한다.
# input_sized에는 총 이미지 사이즈도 잡아줘야 한다. None을 사용하는게 제일 좋다.
model.summary()
```

2. 클래스 사용
```python
import tensorflow as tf
import pandas as pd

# 데이터 준비
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# validation_data 별도로 준비
x_train, x_val = x_train[:48000], x_train[48000:]
y_train, y_val = y_train[:48000], y_train[48000:]

# 모델 학습
model.fit(x_train, y_train, epochs=10, batch_size=128, validation_data=(x_val, y_val))

# 모델 평가
model.evaluate(x_test, y_test)
```