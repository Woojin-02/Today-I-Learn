# 첫째 항 A, 두 항의 차이 B, 몇 번째 항인지 나타내는 N이 입력 되었을 때 N번째의 항을 출력하는 프로그램

a, b, c = map(int, input().split())
answer = a

for i in range(c-1) : 
    answer += b

print(answer)