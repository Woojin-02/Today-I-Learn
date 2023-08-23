# 10진수를 8진수, 16진수로 나누는 코드
# 알파벳은 대문자로 출력
# 입력값 28 출력값 34 1C
# 입력값 99 출력값 143 63

num = int(input())

num8 = oct(num)[2:]
num16 = hex(num)[2:]

print(num8.upper(), num16.upper())