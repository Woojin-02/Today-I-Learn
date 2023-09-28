# Word Embedding

* 고차원 저밀도 백터를 저차원 고밀도 벡터로 변환

### encoding
 * 아날로그를 디지털로 전환하는 것
 * 현실세계에 존재하는 것들을 0과 1로 변환하는 규칙을 encoding, 이걸 역으로 해제하는 것을 decoding이라고 함
 * Embedding을 사용해서 word to vector(Word2Vec) 진행

### Word2Vec
 * 원핫인코딩은 90도(직각) 앵글 값이기 때문에 유사성이 없다.
 * 따라서 유사성을 보존하는 Embedding이 필요.
 * 비슷한 단어끼리는 뭉쳐있다는 가정을 하고 진행한다.

**1. Skip-Gram**
* 중간에 있는 단어들을 입력으로 주변 단어들을 예측하는 방법
* Windows size를 설정해서, 단어 주변에 있는 단어 몇개를 가져올지 결정할 수 있다.
    * window size가 2일 때, 인공신경망 도식화
    * ![image](https://github.com/Woojin-02/Today-I-Learn/assets/64728336/1c0deee8-b98b-4786-9137-42856ba39407)
    * ![image](https://github.com/Woojin-02/Today-I-Learn/assets/64728336/86970323-7393-4c69-9abb-23f782a7dbce)



