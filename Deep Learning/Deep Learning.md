# Deep learning

* Neuaral Network 라고 한다.
* 인공신경망도 같은 의미.
* 머신러닝의 일부이다.
    * 인공지능 > 머신러닝 > 딥러닝
* TensorFlow, PyTorch, Caffe2 등을 이용해 딥러닝을 사용한다.
    * TensorFlow는 파이썬과 조금 다른 점이 있지만, 초심자가 딥러닝을 배우기에 좋다.
    * PyTorch는 파이썬 기반이라 파이썬을 잘 다루면 쓰기 좋다.
    * TensorFlow와 PyTorch 모두 현직에서 사용되고 있다.

```python
# 구글 코랩에서 사용
import pandas as pd
import tensorflow as tf
```

### 딥러닝 과정
**1. 딥러닝 모델 준비(Deep Learning Model Setup)**
* 어떤 model, optimizer, loss등 사용할지 결정한다.

**2. 학습(Training(with Large Scale Dataset))**
* 준비된 데이터셋을 이용해 학습한다.

**3. 추론, 예측(Inference / Testing)**
* 학습된 모델을 이용해 추론한다.

### 딥러닝의 기본 양상
**1. 과거의 데이터를 준비한다.**
```python
x_train = df[['feature']]
y_train = df[['target']]
#확인
print(x_train.shape, y_train.shape)
```

2. 모델의 구조를 만든다.
```python
X = tf.keras.Input(shape=[1])  # shape=[]에 들어갈 값은 독립변수의 수
Y = tf.keras.layers.Dense(1)(X) # Dense()(X)에 들어갈 값은 종속변수의 수

model = tf.keras.Model(X, Y)
model.compile(loss='mse') # 회귀 모델
```

3. 데이터로 모델을 학습(fit)한다.
```python
model.fit(x_train, y_train, epochs=1000, verbose=0) # verbose = 0 : 학습 메시지 가리기
model.fit(x_train, y_train, epochs=5) # epochs : 5번 학습
```
* 이 단계에서 데이터를 학습하면서 loss(로스, 오차)가 줄어든다.
* loss가 더이상 줄어들지 않을때까지 학습한다.

4. 모델을 이용한다.
```python
model.predict([[예측하고싶은 값]])
```

### 딥러닝 공식
* y = W1X1 + W2X2 + ..... + WnXn + b
    * W : 가중치. 이 특징이 최종 판단에 얼마나 중요한지
    * b : 편향. 모든 입력값이 0일 때 기본적으로 가진 값(입력이 들어오지 않아도 기본적으로 가진 값)
* `model.get_weights()` : 가중치, 편향 출력
    * 출력된 가중치와 편향 값을 이용해서 값이 n일때의 예측값을 알 수 있음

### 저장 & 로딩
```python
# 저장
model.save("my_model.keras")
# 로딩
mymodel = tf.keras.models.load_model("my_model.keras")
# 모델 이용
mymodel.predict()
```

