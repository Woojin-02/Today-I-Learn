# 거스름돈을 쿠폰으로 대신할 때, 최소 개수로 쿠폰 지급하기
# 쿠폰 단위는 10, 50, 100, 500, 1000, 5000, 10000, 50000
# 예제 입력 5630, 출력 6

price = int(input())  # 거슬러줘야 하는 금액 입력(10의 배수여야 함)
count = 0

coupon = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 큰 순서대로

for c in coupon :
    count += price // c  # 거스름돈과 쿠폰 가격을 나눴을 때의 몫을 count에 추가
    # print(count, price, coupon)
    price = price % c  # 큰 금액 수만큼 나누고, 그 나머지를 다시 다음 쿠폰값과 나누기 위해 나머지를 구함
    
print(count)