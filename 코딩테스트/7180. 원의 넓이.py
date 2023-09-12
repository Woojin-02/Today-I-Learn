# 원주율(PI)의 값은 소수점 두 자리까지, 즉 3.14
# 원의 반지름이 주어지면 원의 넓이를 출력하는 프로그램
# 소수 부분은 0으로 끝나지 않아야 하며, 답이 정수인 경우 소수 부분을 아예 출력하지 않음
"""
10 -> 314
5 -> 78.5
"""

r = int(input())
pi = 3.14
answer = r * r * pi

if answer.is_integer():
    print(int(answer))
else :
    print(answer)