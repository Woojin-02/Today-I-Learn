# 200kg 이상인 소에게는 A등급을, 180kg 이상인 소에게는 B등급을,
# 150kg 이상은 C등급을 나머지 소들에게는 D등급을 매기는 프로그램

num = int(input())

if num >= 200 : 
    print("A")
elif num >= 180 : 
    print("B")
elif num >= 150 :
    print("C")
else :
    print("D")