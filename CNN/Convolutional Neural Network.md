# Convolutional Neural Network

* 이미지 데이터를 바로 Flatten을 사용해서 데이터의 형태를 바꾸면 위치 정보가 소실됨
* ***위치정보의 소실을 최대한 막으면서 이미지 데이터를 학습하도록 하는 것이 CNN(Convolutional Neural Network)***
* ***원본 이미지(혹은 그로부터 생성된 Feature 맵)의 일부를 분석해서, 그 특징(위치정보가 포함된)으로 새로운 Feature map 생성***

### 1. Feature Map
* 기존에 없던 특징들을 뽑아 그 특징들을 쌓아서 지도의 형태로 만든 것
    * H : 높이
    * W : 너비
    * C : 채널(Depth)
* 하나의 Feature map에는 서로 다른, 기존에 없었던, 기존의 이미지를 보존한 채로 n개의 새로운 feature가 있음
* Feature map size 구하는 공식

![image](https://github.com/Woojin-02/Today-I-Learn/assets/64728336/cf3bd83e-9e4b-4813-a114-9d5f8b29ef6a)


### 2. Feature Map 생성 과정
* 분석하고자 하는 이미지를 조각으로 만들어서 특징을 뽑아냄
* 이때 필요한 것이 Filter
    * 5 X 5 X 1 크기의 흑백 이미지 데이터가 있을 때, 그걸 3 x 3 크기나 2 X 2 크기의 filter로 데이터를 분할해서 특징을 만들 수 있음
    * 3 X 3 크기로 데이터를 훑으면서 랜덤한 어떤 값을 각각 곱하여 구함
    * 이 Filter가 데이터를 거쳐서 만들어진 것을 Feature Map 이라고 함
* Stride 하이퍼파라미터는 filter가 움직이는 폭을 결정할 수 있음
    * (1, 1)이면 가로, 세로로 한칸씩 이동함
* 5 X 5 X 1 크기의 흑백 이미지 데이터를 3 X 3 크기의 filter로 Feature map을 만들면, 만들어진 Feature map은 3X3 크기의 데이터가 만들어짐
* 즉, 데이터가 축소됨
* 이를 방지하기 위해 사용하는 것이 zero padding
    * zero padding(이하 padding)은 데이터의 외곽에 0 데이터를 추가하여 데이터의 크기를 늘림
    * 이를 통해 생성되는 Feature map의 크기를 유지할 수 있고,
    * 외곽 데이터의 정보를 더 많이 훑어보게 되므로 외곽 정보를 더 반영할 수 있음

### 3. 컬러 이미지에서의 CNN
* 32 X 32 X 3 의 컬러 이미지가 있을 때,
    * 생성되는 Filter의 수는 사용자가 임의로 정한다
    * Filter의 크기는 사용자가 임의로 정하되, **채널(depth)는 앞전 데이터의 깊이를 따라간다**
        * 예를 들어 5 X 5 X 3, 7 X 7 X 3은 가능, 5 X 5 X 2는 불가능
    * Padding도 선택사항
    * Activation은 필수
* 결과로 28 X 28 X 32의 Feature Map이 나온다.
    * *생성된 filtermap의 깊이는 앞서 Convolutional Layer를 생성할 때 사용한 Filter의 개수와 같다*
    * 서로 다른 필터 n개를 써서, feature map을 n개 만들기 때문
* 28 X 28 X 32는 패딩하지 않았다고 가정했을 때의 결과다.
* 만약 패딩을 했다면 32 X 32 X 32 라는 Feature map이 나와야 한다.
    * zero padding으로 feature map의 크기를 유지했기 때문이다.

### 4. Pooling Layer
* depth는 유지하고 가로 세로 사이즈만 줄일 때 사용한다
    * 28 X 28 X 128 사이즈 feature map -> 14 X 14 X 128 사이즈 feature map
* 데이터의 빠른 처리를 위해 예전에 사용했으나, 점점 사용하지 않는 추세.
* filter size(예시 : (2, 2)), Stride(예시 (2, 2))를 설정한다.
    * Stride는 filter size와 동일하게 설정하는 것이 국룰
* max pooling과 average pooling이 있다.
    * max pooling은 filter안에 있는 데이터를 뽑아낼 때 가장 큰 값을 뽑아낸다.
    * avg pooling은 filter 안에 있는 데이터들의 평균을 뽑아낸다.

### 5. CNN 순서
각자 차이가 있지만 흐름은 비슷함
```
원본 이미지 -> CONV -> pool -> CONV -> pool -> Flatten -> FC -> FC -> 예측값
```

1. reshape
* 데이터의 형태가 (60000, 28, 28)같이 채널이 없다면, (60000, 28, 28, 1)의 형태로 채널이 추가되어야 한다
```python
train_x.shape, test_x.shape
_, h, w = train_x.shape
train_x = train_x.reshape(train_x.shape[0], h, w, 1)
test_x = test_x.reshape(test_x.shape[0], h, w, 1)
print(train_x.shape, train_y.shape, test_x.shape, test_y.shape)
```

2. 스케일 조정
* 0 ~ 255 사이의 이미지값을 0~1로 스케일링 해야 한다.
```python
print(train_x.max(), train_x.min())

max_n, min_n = train_x.max(), train_x.min()

train_x = (train_x - min_n) / (max_n - min_n)
test_x = (test_x  - min_n) / (max_n - min_n)

print(train_x.max(), train_x.min())
```

3. one-hot Encoding
* 필요에 따라 y_test, y_train 값을 원핫 인코딩해야 한다.
* 만약 원핫인코딩을 하지 않는 경우에는, model을 compile 할 때 `sparse_categorical_crossentropy`를 사용한다.
```python
from tensorflow.keras.utils import to_categorical

class_n = len(np.unique(train_y))

train_y = to_categorical(train_y, class_n)
test_y = to_categorical(test_y, class_n)

# 아래 코드도 가능
train_x = train_x.reshape(train_x.shape[0], 28, 28, -1)
test_x = test_x.reshape(test_x.shape[0], 28, 28, -1)

train_y.shape
```
* 원래대로 되돌리려면
```python
np.argmax(test_y, axis=1)
# 후에 실제 값과 비교할 때 사용함
# 자세한 사항은 아랫줄 '평가 지표 및 실제 데이터 확인'을 참고(shift+f로 찾기)
```

4. 모델링
* 라이브러리
```python
# 라이브러리 불러오기
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.backend import clear_session

from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPool2D, Flatten
from tensorflow.keras.callbacks import EarlyStopping
```

* 세션 클리어
```python
clear_session()
```

* 레이어 엮기
```python
il = Input(shape=[28, 28, 1])
hl = Conv2D(filters=128,            # 새롭게 제작하려는 feature map의 수
            kernel_size=(3, 3),     # convalutional layer filter의 가로세로 크기
            strides=(1, 1),         # convolutional Filter의 이동 보폭
            padding='same',         # 패딩을 하려면 same 입력, 패딩 적용 유무
            activation='relu',      # 활성화 함수 반드시 작성
            )(il)

hl = BatchNormalization()(hl)
hl = Conv2D(filters=128, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu')(il)

hl = BatchNormalization()(hl)
hl = MaxPool2D(pool_size=(2, 2),    # Pooling Filter의 가로세로 크기
               strides=(2, 2)       # Pooling Filter의 이동 보폭 (None은 기본적으로 Pool_size를 따라감))
              )(hl)

hl = Dropout(0.25)(hl)

hl = Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu')(hl)
hl = BatchNormalization()(hl)
hl = Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu')(hl)
hl = BatchNormalization()(hl)
hl = MaxPool2D(pool_size=(2, 2), strides=(2, 2))(hl)
hl = Dropout(0.25)(hl)

hl = Flatten()(hl)
hl = Dense(128, activation='relu')(hl)
ol = Dense(10, activation='softmax')(hl)
```

* 모델의 시작과 끝 지정
```python
model = Model(il, ol)
```

* 모델 컴파일
```python
model.compile(optimizer = 'adam',                # 경사하강법의 세부 방법 설
              loss='categorical_crossentropy',   # 내 모델의 예측값과 실제 정답을 무엇으로 비교할지 결정
              metrics='accuracy'                 # 분류 문제의 모델 지표
             )
```

* EarlyStopping 설정
```python
es = EarlyStopping(monitor='val_loss',       # 얼리스토핑 적용할 관측 대상
                   min_delta=0,              # Threshold. 설정한 값 이상으로 변화해야 개선되었다 간주.
                   patience=3,               # 성능 개선이 발생하지 않을 때, 몇 Epochs 더 볼 것인지.
                   verbose=1,                # 어느 epoch에서 얼리 스토핑이 적용되었는지 보여줌
                   restore_best_weights=True # 가장 성능이 좋게 나온 Epoch의 가중치로 되돌림
                   )
```

* 모델 학습
```python
hist = model.fit(train_x, train_y, epochs=1000, verbose=1,
                 validation_split=0.2, # 학습 데이터로부터 validation set을 20% 생성
                 callbacks=[es]        # 얼리스토핑 적용
                 )
```

* 모델 평가
```python
model.evaluate(test_x, test_y, batch_size=100)
```

* 모델 시각화
```python
if not isinstance(hist, dict) :
    history = hist.history

plt.figure(figsize=(10, 5))
plt.plot(history['accuracy'])
plt.plot(history['val_accuracy'])
plt.title('Accuracy : Training vs Validation')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc=0)
plt.show()
```
```python
if not isinstance(hist, dict) :
    history = hist.history

plt.figure(figsize=(10, 5))
plt.plot(history['loss'])
plt.plot(history['val_loss'])
plt.title('Loss : Training vs Validation')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc=0)
plt.show()
```

* 예측값 생성
```python
y_pred = model.predict(test_x)
y_pred.shape
```

* 평가 지표 및 실제 데이터 확인
```python
y_pred_arg = np.argmax(y_pred, axis=1)  # 원핫 인코딩을 다시 묶음
test_y_arg = np.argmax(test_y, axis=1)  # 원핫 인코딩을 다시 묶음
print(y_pred_arg.shape, test_y_arg.shape)

accuracy_score(single_test_y, single_y_pred) # 정확도 확인
```
