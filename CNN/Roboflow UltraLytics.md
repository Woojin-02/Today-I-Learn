# Roboflow UltraLytics

* 구글 코랩에서 실행
* Roboflow에서 Code 가져오기 실행

### 1. 데이터셋
* Roboflow에서 원하는 모델 검색 후 코드 복사해오기
```python
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="")
project = rf.workspace("sooyounggaonteam").project("gemstone__")
dataset = project.version(9).download("yolov8")
```
```
WARNING: The following packages were previously imported in this runtime:
  [certifi,cycler,pyparsing]
You must restart the runtime in order to use newly installed versions.
```
* 해당 오류가 뜨면 코랩의 런타임-런타임 다시 시작 눌러주면 된다. 오류 아님.

### 2. data.yaml 파일 설정
* 내가 받은 데이터셋 파일
    * train
        * images : `이 폴더의 경로를 넣어주어야함`
        * labels
    * valid
        * images : `이 폴더의 경로를 넣어주어야함`
        * labels
    * test(있을수도 있고 없을수도 있음)
        * images : `이 폴더의 경로를 넣어주어야함`
        * labels
    * data.yaml : 여기에 들어가서 train-images와 valid-images 폴더의 경로를 넣어주어야 한다. test 데이터는 사용하려면 마찬가지로 경로 넣어주고, 별도의 다른 테스트 이미지를 사용하려면 test: 이후를 아예 지운다.

```
data.yaml 예시
train : /content/데이터셋이름/train/images
val : /content/데이터셋이름/valid/images
test : 
```


### 3. 모델링

```python
!pip install ultralytics
from ultralytics import YOLO
```

1. 모델 구조만 빌려오기

```python
# 모델 선언
model_scratch = YOLO(model='yolov8n.yaml', task='detect')

# 모델 학습
# pretrained=False
model_scratch.train(data='/content/gemstone__-9/data.yaml',  # 구글 코랩 내의 data.yaml 파일의 경로를 입력해야 함
                    epochs=100, patience=5, save=True, project='trained_scratch',
                    pretrained=False, optimizer='auto', seed=2023
                    )

# 모델 예측
# 결과는 코랩 내 파일에서 runs 혹은 생성된 학습파일 내에서 확인 가능. 
# 보통 predict라는 이름으로 되어있으니 이 이름을 찾기
model_scratch.predict(source=test_image,
                      conf=0.25,
                      iou=0.7,
                      save=True,
                      line_width=2
                      )
```


2. 모델 구조 + 가중치 빌려오기
```python
# 모델 선언
model_pretrained = YOLO(model='yolov8n.pt', task='detect')

# 모델 학습
# pretrained=True
model_pretrained.train(data='/content/gemstone__-9/data.yaml',
                       epochs=10,
                       patience=3,
                       save=True,
                       project='trained_pretrained',
                       pretrained=True,
                       seed=2023)

# 모델 예측
# 결과는 코랩 내 파일에서 runs 혹은 생성된 학습파일 내에서 확인 가능. 
# 보통 predict라는 이름으로 되어있으니 이 이름을 찾기
model_pretrained.predict(source=test_image,
                         conf=0.25,
                         iou=0.7,
                         save=True,
                         line_width=2)
```