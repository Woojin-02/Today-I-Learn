# 아버지와 어머니의 키의 평균 : 그 자녀의 예상 키
# 아버지와 어머니의 키가 자연수로 각각 주어질 때, 자녀의 예상 키 출력

# 아버지의 키와 어머니의 키를 각각 f, m 변수에 저장함
# int는 변수에 저장될 타입, input()은 입력값을 변수에 저장하는 함수
# split(' ')는 공백(' ')을 기준으로 분할하여 리스트를 생성함
f, m = map(int, input().split(' '))

# 평균 구해서 출력
# // 는 나머지 없는 나눗셈 값 구하기
print((f + m) // 2)