# UltraLytics_YOLOv8

* 다양한 사용방법이 있음
* 여기서는 이 파일의 내용을 Roboflow에 적용해볼 것임(링크)
* 현재 종류 : yolo8n.pt, yolo8n.pt,yolo8s.pt,yolo8m.pt,yolo8l.pt,yolo8x.pt.
     * n이 가장 작은 단위이며 뒤로 갈수록 점점 단위가 커진다. 제일 큰 단위는 x

### 1. 설치 및 import
```python
# 설치
!pip install ultralytics

# 설정
from ultralytics import settings

# 모델
from ultralytics import YOLO
```

### 2. 모델 선언

* 모델의 구조와 해당 구조에 맞게 사전 학습된 가중치를 불러온다.
* 권장사항은 모델 구조 + 가중치를 전부 가져와서 그대로 쓰거나 fine-tuning 하는 것이다.
* Parameters
    * model : `모델 구조(.yaml)` 또는 `모델 구조 + 가중치 설정(.pt)`. task와 맞는 모델을 선택해야 한다.
    * task : detect, segment, classify, pose 중 택일
```python
model = YOLO(model='yolov8n.pt', task='detect')
```

### 3. 모델 학습

* Parameters
    * *data* : 학습시킬 데이터셋의 경로. default 'coco128.yaml'
    * *epochs* : 학습 데이터 전체를 총 몇 번씩 학습시킬 것인지 설정. default 100
    * *patience* : 학습 과정에서 성능 개선이 발생하지 않을 때 몇 epoch 더 지켜볼 것인지 설정. default 50
    * batch : 미니 배치의 사이즈 설정. default 16. -1일 경우 자동 설정.
    * imgsz : 입력 이미지의 크기. default 640
    * *save* : 학습 과정을 저장할 것인지 설정. default True
    * project : 학습 과정이 저장되는 폴더의 이름.
    * name : project 내부에 생성되는 폴더의 이름.
    * exist_ok : 동일한 이름의 폴더가 있을 때 덮어씌울 것인지 설정. default False
    * *pretrained* : 사전 학습된 모델을 사용할 것인지 설정. default False
    * optimizer : 경사 하강법의 세부 방법 설정. default 'auto'
    * verbose : 학습 과정을 상세하게 출력할 것인지 설정. default False
    * seed : 재현성을 위한 난수 설정
    * resume : 마지막 학습부터 다시 학습할 것인지 설정. default False
    * freeze : 첫 레이어부터 몇 레이어까지 기존 가중치를 유지할 것인지 설정. default None

```python
model.train(data='coco128.yaml',  # 따로 dataset을 지정하거나 디폴트 dataset 사용 가능
            epochs=10,
            patience=5,
            save=True,
            project='trained',
            name='trained_model',
            exist_ok=False,
            pretrained=False,
            optimizer='auto',
            verbose=False,
            seed=2023,
            resume=False,
            freeze=None
            )
```

* pretrained를 True로 설정하면 모델 구조 + 가중치 설정(.pt) 방법을 사용하고,
* pretrained를 False로 설정하면 모델 구조(.yaml)만 쓰는 방법을 사용한다.


### 4. 모델 검증

```python
model.val()
```

### 5. 모델 평가(예측값 생성)
* Parameters
    * source : 예측 대상 이미지/동영상의 경로
    * conf : confidence score threshold. default 0.25
    * iou : NMS에 적용되는 IoU threshold. default 0.7. threshold를 넘기면 같은 object를 가리키는 거라고 판단.
    * save : 예측된 이미지/동영상을 저장할 것인지 설정. default False
    * save_txt : Annotation 정보도 함께 저장할 것인지 설정. default False
    * save_conf : Annotation 정보 맨 끝에 Confidence Score도 추가할 것인지 설정. default False
    * line_width : 그려지는 박스의 두께 설정. default None

```python
model.predict(source='test데이터 경로 혹은 이미지 주소',
              save=True, 
              save_txt=True, 
              line_width=2)
```
