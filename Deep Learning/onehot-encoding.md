# Onehot- Encoding

* 데이터를 수많은 0과 한개의 1의 값으로 데이터를 구별하는 인코딩
* 범주형 데이터는 딥러닝 알고리즘으로 학습할 수 없으므로, 범주형 데이터를 숫자형으로 바꿀때 사용
* 예를 들어, 범주형 데이터로 부속기기 칼럼에 키보드, 마우스가 있을 때 수치형으로 바꾼다고 가정
    * 키보드, 마우스라는 2개의 칼럼으로 나누고, 키보드가 있는 데이터는 키보드에 1, 마우스에 0
    * 마우스가 있는 데이터는 마우스에 1, 키보드에 0이 있는 식이다.
    * [1, 0]
    * [0, 1]

---

* 원핫인코딩을 거치면 데이터의 종속변수가 2개 이상으로 증가한다.
* 따라서, param도 (x의 개수 * y의 개수) + y의 개수가 된다.
    * param은 `model.summary()`로 확인 가능
    * 종속변수가 2개 이상이면, 
```python
X = tf.keras.Input(shape=[4])
Y = tf.keras.layers.Dense(3, activation="softmax")(X) # 종속변수가 3개라서 3, activation 추가(분류일 경우에만)
model = tf.keras.Model(X, Y)
model.compile(loss="categorical_crossentropy", metrics="accuracy") # loss 계산방식 변경, 사람이 이해하기 쉽도록 정확도(accuracy) 출력
```

---

1. softmax
* 종속변수 개수가 2개 이상일 때

```python
X = tf.keras.Input(shape=[4])
Y = tf.keras.layers.Dense(3, activation="softmax")(X)
model = tf.keras.Model(X, Y)
model.compile(loss="categorical_crossentropy", metrics="accuracy")
```

2. sigmoid
* 종속변수 개수가 1개일 때(ex : 남(0), 여(1))

```python
X = tf.keras.Input(shape=[4])
Y = tf.keras.layers.Dense(3, activation="sigmoid")(X)
model = tf.keras.Model(X, Y)
model.compile(loss="binary_crossentropy", metrics="accuracy")
```

3. 활성화 함수
* 앞에 나온 결과값을 뒤의 뉴런으로 넘길지 판단해서 넘길지 결정하는 함수
* 만약 뉴런이 뒤로 신호를 보내는 데에 자격미달이면 활성화되지 않음. 즉, 활성화를 결정하기 때문에 활성화 함수임
* 뉴런의 연결 중간중간에서는 활성화 함수, 최종(출력단)단에서, 데이터가 회귀 모델이냐 분류 모델이냐에 따라 Identity(회귀)이거나 Softmax(분류)를 사용함
* 활성화 함수에 회귀모델, 분류모델에 따라 함수(Softmax등..)를 넣으면
    * -> 회귀는 입력(결과값)을 그대로 전달 / 분류는 입력(결과값)을 0~1(확률값)으로 바꿔서 전달