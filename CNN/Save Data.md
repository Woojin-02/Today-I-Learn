# 모델 저장 & 불러오기

1. 모델을 학습시키기 전에 아래 코드를 작성한다.
```python
# model checkpoint
from tensorflow.keras.callbacks import ModelCheckpoint

mcp = ModelCheckpoint(filepath='/content/model1.h5',   # 모델 저장 경로
                      monitor='val_loss',              # 모델 저장의 관심 대상
                      verbose=1,                       # 어느 시점에서 저장되는지 알려줌
                      save_best_only=True,             # 최고 성능 모델만 저장
                      save_weights_only=False)         # True : 가중치만 저장 | False : 모델 구조 포함하여 저장
```

2. 모델을 학습한다.

3. 모델을 저장한다.

```python
# h5 파일로 저장.
model1.save('save.h5')
```

4. 모델을 불러온다.

```python
clear_session()
model = keras.models.load_model('save.h5')
model.summary()
```

5. 모델을 사용한다.
* 모델 가중치 확인
```python
model.get_weights()[0][0][0]
```
* 모델 예측
```python
# 모델을 사용하여 학습 데이터(train_x) 및 테스트 데이터(test_x)를 예측
pred_train = model.predict(train_x)
pred_test = model.predict(test_x)

# 예측 결과에서 각 클래스에 대한 가장 확률이 높은 클래스의 인덱스를 선택
single_pred_train = pred_train.argmax(axis=1)
single_pred_test = pred_test.argmax(axis=1)

# 학습 데이터와 테스트 데이터에 대한 실제 레이블(train_y, test_y)과 예측 레이블(single_pred_train, single_pred_test)을 사용하여 정확도를 계산

# 학습 데이터에 대한 정확도 계산
logi_train_accuracy = accuracy_score(train_y.argmax(axis=1), single_pred_train)

# 테스트 데이터에 대한 정확도 계산
logi_test_accuracy = accuracy_score(test_y.argmax(axis=1), single_pred_test)

# CNN 모델의 성능 출력
print('CNN')
print(f'트레이닝 정확도 : {logi_train_accuracy*100:.2f}%')  # 학습 데이터에 대한 정확도를 소수점 두 자리까지 출력
print(f'테스트 정확도 : {logi_test_accuracy*100:.2f}%')    # 테스트 데이터에 대한 정확도를 소수점 두 자리까지 출력
```