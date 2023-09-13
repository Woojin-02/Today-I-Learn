# 자연수 N 이하의 소수 개수를 출력하는 프로그램
# 소수= 양의 약수가 자기 자신과 1만 존재하는 수
# 어떤 정수 A가 어떤 정수 B의 약수라는 것은 B를 A로 나누었을 때 나누어떨어짐을 의미
# 첫 번째 줄에 1 이상 1000 이하의 자연수 N이 주어집니다.
# 1 이상 N 이하의 자연수 중에서의 소수의 개수를 출력합니다.

n = int(input())
count = 0
lists = []

for i in range(2, n+1) :
    p = True
    for j in lists:
        if i % j == 0:
            p = False
            break
        elif j > i**0.5:
            break
    if p:
        lists.append(i)

print(len(lists))