# 최대공약수란 어떤 두 개 이상의 자연수들이 있을 때, 두 수의 공통된 약수 중 가장 큰 수
# 서로 다른 두 자연수 N, M이 주어졌을 때, 두 수의 최대공약수를 출력하는 프로그램
"""
예제 1 : 124 512 -> 4
예제 2 : 14 18 -> 2
예제 3 : 10 20 -> 10
"""

# 방법 1
a, b = map(int, input().split(' '))
list_a = []
list_b = []

for i in range(1, a+1):
    if a % i == 0:
        list_a.append(i)
for i in range(1, b+1):
    if b % i == 0:
        list_b.append(i)
        
# print(list_a)
# print(list_b)

answer = []

for i in list_a:
    if i in list_b:
        answer.append(i)
        
#print(answer)
print(max(answer))


# 방법 2
import math

a, b = map(int, input().split(' '))
print(math.gcd(a, b))