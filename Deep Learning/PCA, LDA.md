# PCA/LDA

### 1. 차원의 저주
* 차원을 무조건 많이 생성한다고 해서 성능이 올라가는 것이 아니며, 오히려 불필요하게 차원이 많으면 공간이 낭비되서 효율이 떨어진다.
* 그렇기 때문에 차원을 축소하는 작업이 필요하다.
  
![image](https://github.com/Woojin-02/Today-I-Learn/assets/64728336/5145a598-97af-4065-8ac6-5d54463f095c)


### 2. 차원 축소
* 차원 축소는 행렬곱 연산으로 이루어진다. 이때, 어떤 방향으로 축소하는지에 따라 PCA, LDA 두가지로 나뉜다.
* 어떤 방향으로 1차원 변환 시키느냐에 따라 원래 정보를 최대한 온존하되 넓게 퍼지는 데이터의 모습이 되느냐(PCA),
아니면 원래 데이터의 특정은 고민하지 않고 분류가 되기 쉽게 두드러지는 특징만 남긴 데이터의 모습이 되느냐(LDA)가 결정된다.

![image](https://github.com/Woojin-02/Today-I-Learn/assets/64728336/231fbcaa-63a3-4349-8208-a480519e2edf)


**1. PCA(Principal Components Analysis)**
* 2차원에서 1차원으로 바꿀 때 잃어버리는 정보가 최소한이 되도록 넓게 축소

  ![image](https://github.com/Woojin-02/Today-I-Learn/assets/64728336/d94c3860-39f2-4d92-adfb-4a26f2c5b6ec)


**2. LDA(Linear Discriminant Analysis)**
* 분류가 제일 잘 되는 방향으로 2차원 을 1차원으로 변환
* 데이터가 뭉쳐있을수록(=표준편차가 작을수록), 서로 다른 데이터가 멀리 있을 수록 분류가 잘되기 때문에, 차원을 축소할 때 평균을 뺀 값은 클수록 좋고, 분산은 적을 수록 좋다.

  ![image](https://github.com/Woojin-02/Today-I-Learn/assets/64728336/68ae1b0b-2b5c-4c62-a672-99c4d7e9b41a)
