# Overfitting(과대적합)

* 통계 모델이 학습 데이터와 정확히 일치하는 경우
* 학습 데이터에 지나치게 적응하여 테스트 데이터의 예측이 지나게 떨어진다.

---

**해결 방법**
1. Dropout
   
2. Autoencoding
   * 필요없는(특이한) 특징을 날리기 위해 행렬을 줄였다가 다시 늘려서 사용하는 방법
   * PCA와 굉장히 유사(중요한 특징들을 남겨두기 때문에)

  ![image](https://github.com/Woojin-02/Today-I-Learn/assets/64728336/d4ebdeaa-b49d-4aa9-a5c7-c367a86bb374)


* 참고
DropOut은 훈련 과정에서 무작위로 선택한 일부 뉴런(또는 뉴런의 출력)을 비활성화(dropout)하여 모델을 학습시킬 때 특정 뉴런들에 과도하게 의존하지 않도록AutoEncoding은 데이터의 중요한 특징만 추출하도록 한다.</br>
개발자는 Dropout이 편하고, 연구자는 AutoEncoding이 통계학적으로 더 좋다.
