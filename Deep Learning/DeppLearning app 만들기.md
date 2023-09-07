# 딥러닝 앱 만들기

### 1. Hugging Face 라이브러리
* Github와 같음
* 학습된 모델들의 가중치를 라이브러리에 업데이트함
* 모델을 내 컴퓨터에 다운로드 받아서 서비스 실행

#### 1. 라이브러리 설치

* transformer -자연어처리
* datasets -데이터셋
* xformers -트랜스포머가속기

```python
# 트랜스포머, 데이터셋, 텐서플로우 라이브러리 설치
!pip install transformers datasets xformers -q
```

#### 2. 파이프라인(pipeline)
* 모델을 사용하는 가장 쉽고 빠른 방법
* 자연어 처리, 음성 인식, 컴퓨터 비전 및 멀티 모달 등 다양한 작업에 사용
* 작업(Task) 선택 -> 모델 선택 -> 모델 이용 3단계로 이용

- https://huggingface.co/models
- 이 링크를 통해 모델 다운로드 가능
- 아래 예시 이외에 많은 모델들이 존재함

|Task|Description|Pipline idenifier|
|:---:|:---:|:---:|
|Text classification|텍스트 분류|pipeline(task=“sentiment-analysis”)|
|Text generation|입력한 프롬프트에 이어지는 텍스트 생성|pipeline(task=“text-generation”)|
|Summarization|텍스트 또는 문서에 대한 요약|pipeline(task=“summarization”)|
|Image classification|이미지 분류|pipeline(task=“image-classification”)|
|Image segmentation|이미지의 개별 픽셀 단위 분류|pipeline(task=“image-segmentation”)|
|Object detection|이미지에서 객체탐지 및 클래스 예측|pipeline(task=“object-detection”)|
|Audio classification|오디오 데이터 분류|pipeline(task=“audio-classification”)|
|Automatic speech recognition|음성을 텍스트로 변환|pipeline(task=“automatic-speech-recognition”)|
|Visual question answering|이미지에 대한 질문에 답변|pipeline(task=“vqa”)|
|Document question answering|문서에 대한 질문에 답변|pipeline(task="document-question-answering")|
|Image captioning|이미지에 대한 설명 생성|pipeline(task="image-to-text")|

#### 3. 모델 사용 예시
* 감정 분류
```python
# hugging face의 url 일부를 입력(https://huggingface.co/matthewburke/korean_sentiment)하면 해당 모델 사용 가능
classifier = pipeline("sentiment-analysis", "matthewburke/korean_sentiment")

# 한국어 감정 분류
classifier(["오늘 시험 성적을 100점 받았어!", "오늘 엄마랑 싸웠어. 나보고 게임은 그만하고 공부 좀 하래."])
# [{'label': 'LABEL_1', 'score': 0.9000598192214966}, 긍정
# {'label': 'LABEL_0', 'score': 0.9518436789512634}] 부정
```

#### 4. Gradio
* 딥러닝 엔지니어가 앱을 쉽게 만들 수 있도록 도와주는 프레임워크
* API까지 함께 제공함

```python
!pip install gradio -q
```

* 자세한 사용법은 `https://www.gradio.app/guides` 확인

### 2. Open AI
* 모델을 다운로드 받을 수 없음
* 모델을 이용해서 무언가를 만들 수는 있게 함