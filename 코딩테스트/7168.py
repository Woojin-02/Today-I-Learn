# 100 이상의 정수 N을 각각 5와 7로 나누었을 때의 나머지 중 더 큰 나머지 출력
# 예제 입력 37, 출력 2
# 예제 입력 9995, 출력 6

num = int(input())
print(max(num % 5, num % 7))