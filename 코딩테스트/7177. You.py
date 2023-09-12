# You라고 입력하면 Me, 그 외의 모든 경우의 입력에는 No 라고 답하는 챗봇이 있을 때, 
# 챗봇에 문자열 A를 입력했을 때 챗봇이 답한 문자열을 출력하는 프로그램

# 예제입력 = Are you? 출력 = No
# 예제입력 = You 출력 = Me

a = input()

if a == "You" :
    print("Me")
else :
    print("No")