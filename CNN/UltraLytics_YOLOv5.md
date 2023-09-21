# YOLOv5

* 구글 코랩 기준

### 사용법

1. 모델 라이브러리 설치
```python
!git clone https://github.com/ultralytics/yolov5  # clone
!pip install -r yolov5/requirements.txt  # instal
```

2. 모델 구조 + 가중치 이용해서 학습하기
```python
!python '/content/yolov5/train.py' --img 640 --epochs 3 --data '/content/Dataset/money.yaml' --weights yolov5s.pt --project '/content/Dataset' #--exist ok : 파일 덮어쓰기
```