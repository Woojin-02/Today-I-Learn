# 영덕의 영어 이름을 포함한 N명의 이름이 적힌 목록이 주어집니다.
# 이때 영덕의 영어 이름이 목록에서 몇 번째인지 출력하는 프로그램을 작성하시오
# 첫째 줄에 목록에 적힌 이름의 수 N과 영덕의 영어 이름이 공백을 구분으로 주어집니다. (1 ≤ N ≤ 100)
#둘째 줄에 목록에 적힌 N개의 이름이 공백을 구분으로 주어집니다.
#모든 이름은 길이가 1 이상 100 이하이며 영어 대문자 알파벳으로만 이루어져 있습니다.
#목록에 영덕의 영어 이름은 반드시 있으며 동명이인이 없음을 보장합니다.
#영덕의 영어 이름이 몇 번째에 등장했는지 출력하세요.

N, name = input().split()
N = int(N)

names = input().split()

index = names.index(name) + 1  # 목록은 0부터 시작하지 않으므로 +1

print(index)




