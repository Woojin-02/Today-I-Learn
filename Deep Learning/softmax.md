# Softmax

### 작동 원리
1. 작동 원리

```python
import math

y1=1.8
y2=2.5
y3=-1.1

ey1 = math.e ** y1
ey2 = math.e ** y2
ey3 = math.e ** y3

sum = (ey1 + ey2 + ey3)

py1 = ey1 / sum
py2 = ey2 / sum
py3 = ey3 / sum

print( py1, py2, py3 )
```

* y1, 2, 3을 로짓값이라고 부름.-무한대에서 무한대 사이로 나올 수 있는 어떤 수치값이며, softmax 계산 이전에 만들어지는 값이다.
* ey1, 2, 3은 softmax를 적용하기 위해서, y1,2,3값을 양수로 만들기 위해 math.e를 통해 지수를 곱하는 값을 저장한다.
* py1,2,3이 해당 클래스일 확률을 의미한다.
    * py1값은 y1 클래스가 맞을 확률, py2값은 y2 클래스가 맞을 확률, py3값은 y3 클래스가 맞을 확률을 구하는데, 이때 py1, 2, 3을 모두 더하면 1이 된다.

2. 예시 코드
* model.get_weights()로 알아낸 가중치가 아래와 같을 때
    [array([[ 1.1652668 ,  0.68477255, -0.31088394],
        [ 0.9673362 , -0.46630055, -0.8896154 ],
        [-2.5762677 , -0.39970636,  0.8633284 ],
        [-1.9235661 ,  0.01156936,  1.676738  ]], dtype=float32),
    array([ 1.0496502 ,  0.48568064, -0.92698383], dtype=float32)]

* 아래와 같이 계산하면 softmax 함수를 활용한 결과와 똑같이 나온다.

```python
x1, x2, x3, x4 = 5.1, 3.5, 1.4, 0.2

y1 = 1.1652668 * x1 + 0.9673362 * x2 + -2.5762677 * x3 + -1.9235661 * x4 + 1.0496502 
# w1,2,3,4를 곱하고 b를 더함
y2 = 0.68477255  * x1 + -0.46630055 * x2 + -0.39970636 * x3 + 0.01156936 * x4 + 0.48568064   
y3 = -0.31088394 * x1 + -0.8896154 * x2 + 0.8633284 * x3 + 1.676738 * x4 + -0.92698383

print(y1, y2, y3)

ey1 = math.e ** y1
ey2 = math.e ** y2
ey3 = math.e ** y3

py1 = ey1 / (ey1 + ey2 + ey3)
py2 = ey2 / (ey1 + ey2 + ey3)
py3 = ey3 / (ey1 + ey2 + ey3)

print(py1, py2, py3)
```