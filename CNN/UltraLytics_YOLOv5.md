# YOLOv5

* 구글 코랩 기준
* [YOLOv5 GitHub](https://github.com/ultralytics/yolov5/tree/master), [YOLOv5 Docs](https://docs.ultralytics.com/yolov5/)
* YOLOv5 문서의 튜토리얼에 사용방법과 코드가 상세히 설명되어 있으니 반드시 참고할 것!

### 1. 사전 작업
**1. Dataset**

![image](https://github.com/Woojin-02/Today-I-Learn/assets/64728336/e5fb1de9-9650-44cc-a41d-712683dd0a47)
 * 이 이미지처럼 트리 형식의 구조여야 한다.
 * `images`와 `labels`가 같은 level에 있어야 한다.
 * `images`에는 이미지 파일, 'lables`에는 annotation 파일이 저장되어야 한다.
 * 각각의 파일들을 `train`과 `validation`으로 분류해서 넣는다.

**2. yaml 파일 생성**
* 학습할 클래스 이름 정보 : names
* 학습할 클래스 수 정보 : nc
* Training, Validation, Test 데이터셋 위치 정보(절대 경로 혹은 상대경로로 입력)
* 입력 순서는 상관하지 않아도 된다
* labels의 경로는 입력하지 않아도 된다.
* 저장 위치는 상관 없다.
* 이미지 예시

![image](https://github.com/Woojin-02/Today-I-Learn/assets/64728336/3464819d-0817-44e7-ada2-b0fdd65580ba)

위의 이미지는 아래의 코드로 만들어짐
```python
import yaml

won_dict = {0:'10', 1:'50', 2:'100', 3:'500', 4:'1000', 5:'5000', 6:'10000', 7:'50000'}

yaml_data = {
    'names': won_dict,
    'nc': 8,
    'test': '',
    'train': '/content/Dataset/images/train',
    'val': '/content/Dataset/images/val'
}

with open('/content/Dataset/money.yaml', 'w') as f :
    yaml.dump(yaml_data, f, default_flow_style=False)
```


### 2. 모델 학습

**1. 모델 라이브러리 설치**
```python
!git clone https://github.com/ultralytics/yolov5  # clone
!pip install -r yolov5/requirements.txt  # install
```

**2. YOLOv5 모델 가중치 설치**
* 가중치만 따로 다운로드 받기
```python
!wget https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt
```

**3. 시각화(선택사항)**
* comet 사용
* YOLOv5 공식 Docs, [comet YOLOv5 Docs](https://www.comet.com/docs/v2/integrations/third-party-tools/yolov5/) 참고
* comet 페이지 로그인 후 API 키 받아서 아래 코드에 입력
```python
pip install comet_ml  # 1. install
export COMET_API_KEY=<XwcbPRs4gEoS16pgeoufTLKyx>  # 2. paste API key
```

**4. 모델 구조 + 가중치 이용해서 학습하기**
* **python** : train.py의 경로
* **--img** : 입력 이미지 크기 resize. 640 권장되나 이미지가 클 경우에 한해서만 1280 권장. 이미지 크기가 커질수록 정확도 UP, 속도 DOWN
* --batch : 원하는 배치 크기. 너무 많은 배치를 적요하면 터질 수 있으니 주의
* **--epochs** : 몇번 epochs할지 지정
* **--data** : yaml 파일 경로 지정
* **--weights** : pretrained weights 파일 읽어오기. 처음 실행 시 .pt 파일이 없으면 다운로드도 함께 실행
* **--project** : 학습 완료된 weight 파일 및 성능 평가 데이터 저장. 상위 폴더(저장경로)
* --name : 학습 완료된 weight 파일 및 성능 평가 데이터 저장. 하위폴더(저장될 이름). 없어도 된다. name을 지정하지 않으면 exp가 기본으로 지정된다.
* --exist-ok : 최신 파일이 기존파일을 덮음. 사용하지 않으면 학습할 때마다 새로운 exp1, exp2 파일이 생성됨

```python
# 예
!python '/content/yolov5/train.py' --img 640 --batch 8 --epochs 3 --data '/content/Dataset/money.yaml' --weights yolov5s.pt --project '/content/Dataset' -- name 'trained_detect' --exist-ok
```

```
- 만약 finetuning을 원한다면
   * 학습 완료시 생성되는 weights 파일에서 best.pt 파일을 --weights 부분에 넣고 실행

- 만약 earlyStopping을 수정하고 싶다면
   * 다운로드받은 YOLOv5 파일에 있는 utils -> torch_utils.py 수정
   * 혹은 `--patience 숫자값`을 학습 코드에 추가해서 성능 개선이 발생하지 않을 때 몇 epoch 더 지켜볼 것인지 설정
   * [참고](https://github.com/ultralytics/yolov5/blob/master/utils/torch_utils.py)
- comet 실행 결과를 사이트에서 보고 싶으면 실행창 제일 아래에 뜨는
To upload this offline experiment, run:
    comet upload /content/.cometml-runs/9e382ed7f4ab4504929608fccd742496.zip
메세지 확인해서 실행
```

**5. 모델 평가하기**
* **source** : dectect를 실행하고자 하는 이미지 경로를 적어줌
* conf : confidence score. 0.25이상일 때 바운딩 박스를 그리도록 설정
* weights : weights 파일을 best.pt 가중치 파일을 사용
* iou : Intersection over Union
* project : 데이터가 저장될 상위경로
* name : 데이터가 저장될 하위경로
* line-thickness : 그려질 선의 두께
* exist-ok : 데이터 갱신해서 저장(새로운 파일을 만들지 않음)

```python
!python '/content/yolov5/detect.py' --source 파일 경로 --weights '/content/Dataset/exp/weights/best.pt' --conf 0.25 --iou 0.75 --project '/content/Dataset' --name=run_image --line-thickness 2 --exist-ok
```
