# Image Data Augmentation(이미지 데이터 증강)

* 현실에서는 문제를 해결하기에 적합한 이미지가 없음
* 데이터를 수집해도 양이 부족하거나 저작권에 걸릴 수 있음
* 데이터의 양도 충분하고 저작권도 문제없어도 학습 성능이 잘 나온다는 보장 없음
* 수집한 것만이라도 어떻게든 양을 늘려서 성능을 높이자!
* augmentation을 해서 데이터가 부족할 때 생길 수 있는 편향된 모델이 생성되는 문제를 해결하는 것이 목적

### Image Data Augmentation

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 전부 다 사용할 필요 없음
aug = ImageDataGenerator(rotation_range=50,      # 이미지 회전
                         width_shift_range=0.3,  # 이미지 좌우 이동
                         height_shift_range=0.3, # 이미지 상하 이동
                         zoom_range=0.8,         # 확대/축소 범위
                         shear_range=0.5,        # 비스듬히 늘림
                         horizontal_flip=True,   # 가로 전환
                         vertical_flip=True,     # 세로 전환
                         fill_mode='nearest')    # 마지막 옵션 주의하자. 이미지 회전, 이동, 축소할 때 발생하는 공간을 채우는 방식

imageGen = aug.flow(image, # 이미지 어레이를 받아서.
                    batch_size=1, # 이미지 1장씩
                    # save_to_dir='output', # ouput 이라는 디렉토리 안에
                    # save_prefix='image',  # image라는 단어가 붙어서
                    # save_format='jpg'     # jpg 양식으로 저장
                    ) 
```

```python
from tensorflow.keras.preprocessing.image import ImageDateGenerator

# 학습용 데이터
train_IDG = ImageDataGenerator(rescale=1./255,
                               zca_whitening=True,
                               rotation_range=10,
                               zoom_range=0.1,
                               width_shift_range=0.1,
                               height_shift_range=0.1,
                               horizontal_flip=True
                               vertical_flip=True)
train_IDG.fit(train_x)

flow_train_IDG = trian_IDG.flow(train_x, train_y,
                                batch_size=128,)

# 검증용 데이터
val_IDG = ImageDataGenerator(rescale=1./255)

flow_val_IDG = val_IDG.flow(val_x, val_y,
                            batch_size=128)
```

* 클래스에 맞게 적절히 이미지가 분류되어 만들어진 폴더가 있다면 .flow_from_directory()를 사용할 수 있다.
