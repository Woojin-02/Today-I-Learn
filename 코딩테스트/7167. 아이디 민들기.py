# 아이디가 20글자 미만이고 영어 대소문자로만 쓰여있으면 P, 아니면 I 출력

ids = input()

if len(ids) < 20 and ids.isalpha() :
    print("P")
else : 
    print("I")