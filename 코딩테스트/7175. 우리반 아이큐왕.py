# 학생들의 이름과 IQ가 입력될 때, IQ가 높은 순서대로 상위 3명의 이름을 출력하는 프로그램
# IQ가 같을 경우에는 먼저 입력된 학생의 이름을 출력
"""
예제입력
4
jung 51
dong 160
back 120
pang 89
"""

num = int(input())
dic = {}

for i in range(num) :
    name, iq = input().split(' ')
    iq = int(iq)
    dic[name] = iq
    
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for i in range(min(3, len(dic))):
    print(dic[i][0])