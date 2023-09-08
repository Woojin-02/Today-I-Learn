# 토큰과 임베딩, VectorDB

### 1. 토큰

```import
from transformers import GPT2LMHeadModel, PreTrainedTokenizerFast

# 토큰화 함수
tokenizer = PreTrainedTokenizerFast.from_pretrained("taeminlee/kogpt2")
# 다음 단어 함수
model = GPT2LMHeadModel.from_pretrained("taeminlee/kogpt2")
```

1. 토큰
* 뜻을 지니는 가장 작은 단위의 단어 조각
    * 형태소 분석을 한게 아님!

2. 토큰화
* 토큰을 만드는 방법
* 의미를 지니는 가장 최소단위를 찾는 것이 가장 좋음
* 토큰화 방법 예시
    * 최소 단위로 단어를 쪼개고
    * 토큰에 고유한 번호를 붙인다
    * '안녕? 나는 학생이야' -> ['안녕', '?', '나', '는', '학생', '이야'] -> [14998, 47774, 3918, 835, 7781, 47440]

```python
text = "안녕? 나는 학생이야."
tokens = tokenizer.encode(text, return_tensors="pt")
# 주어진 text를 토큰화하고, 토큰 ID로 변환
# return_tensors="pt"는 반환되는 결과를 PyTorch 텐서로 반환하도록 지정하는 매개변수
tokens
```

3. GPT
* GPT 모델은 토큰을 사용해서 다음에 올 단어를 예측하는 AI
* 자동으로 문맥은 유지하도록 바로 앞 토큰 뿐 아니라 모든 토큰을 고려해서 다음 단어 함수를 계산
* 가장 관련이 있을 것 같은 토큰들의 확률을 구해서, 확률이 가장 높은 것을 출력

```python
# 제일 큰값(확률이 높은)의 토큰 위치를 출력
outputs = model(tokens)[0][0, -1, :] # 모든 토큰들의 확률값
print(outputs[0].shape)
print(outputs) # 여기 값에서 확률을 구해서 가장 높은 확률의 확률을 구함
len(outputs)

token = outputs.argmax(-1) # 가장 높은 확률의 토큰 # outputs에서 가장 큰 값(가장 높은 확률)을 가지는 토큰의 인덱스 찾기
decoded = tokenizer.decode(token) # tokenizer를 사용하여 선택된 토큰을 다시 원래의 텍스트로 디코딩
print(token, decoded)

# </s>가 결과로 나오면 문장 종료의 의미
```

### 2. 임베딩

* 토큰(단어)들과의 연관성(관계)을 어떻게 표현할까?
* 토큰들 간의 관계가 표현된 수로 바꿔서(데이터를 수치화해서) 데이터 공간 상에서 서로 가까이 위치한 토큰을 찾음
* 임베딩은 토큰들 사이의 관계를 표현하기 위한 방법

1. 임베딩
* 특정 차원의 데이터를 내가 원하는 차원으로 옮기는 것
    * = 정보를 데이터공간의 벡터로 표현
* 원핫인코딩으로 5만개의 칼럼을 만들 수는 없기 때문에 하나의 고유한 값을 특정 차원의 숫자값으로 치환시킴
* 임베딩 함수를 통해서 구해진 특정 차원의 숫자값을 입력값으로 사용해서 학습을 시킴
* 토큰을 공간속의 점으로 적절하게 옮긴다 = 공간상의 특정 포인트로 데이터를 적절하게 옮긴다
* 임베딩 레이어의 학습과정
    * 10차원 공간에 5만개의 점을 랜덤하게 찍음
    * -> 점을 조금씩 옮기면서 loss가 최소가 되도록 조정함(그것이 weigth가 됨)
    * -> loss가 최소가 되면 각 점들을 있어야 할 장소로 이동 = 즉, 모델이 스스로 벡터를 만듦.

### 3. Vector DB
* 임베딩된 데이터를 모아둔 DB
* 임베딩 벡터로 데이터를 표현하고 싶을 때 사용

1. 개요
* 그림, 음성, 텍스트 등 비정형 데이터는 테이블 형태의 데이터로는 표현 하기 힘듦
* 벡터값들을 저장하는 DB가 필요함
* 이전에도 있던 개념이지만, 인간의 인지를 넘어선 범위어서 잘 활용되지 못하다가 딥러닝이 나온 후 각광받음

2. 설명
* 결론이 도출되기 직전의 벡터들(마지막 히든레이어의 벡터)는 임베딩된 데이터와 같음
    * 예를 들어, 784차원의 데이터를 84차원의 데이터로 임베딩했을 때, 이 데이터는 10차원의 결과 데이터를 만들 수 있을 정도로 특징이 잘 표현되었다는 뜻이기 때문

2. 사용
* 크로마DB, langchain, huggingface 등을 이용해서 사용
* 생성된 DB 데이터를 GPT에 제공하면 데이터를 기반으로 한, 정확성있는 답이 출력되는 챗봇을 만들 수 있음
* 그 외에도 활용법은 다양함

```python
!pip install langchain openai huggingface_hub -q
!pip install sentence_transformers chromadb -q
```

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# 문장을 임베딩 벡터로 만들어주는 함수(huggingFace)
# "jhgan/ko-sbert-sts"

examples = [] # 원하는 정보(법학, 의료, 공학, 컴퓨터 부품 등) 입력

db = Chroma.from_texts(
    collection_name="sample",  # DB 이름
    texts=examples,
    embedding=HuggingFaceEmbeddings(model_name="jhgan/ko-sbert-sts")
)
```

```python
# examples에 저장되어 있지 않은 질문을 해도 비슷한 내용을 가지고 있는 문서를 출력함
# 임베딩 벡터가 잘 뽑혀있으면 비슷한 텍스트를 찾을 수 있음
question = "미국의 수도는 어디인가요?"
doc = db.similarity_search(question, k=1) # k = 개수 (1개 찾기, 2개 찾기, 3개 찾기 ...)
print(doc[0].page_content)
```

