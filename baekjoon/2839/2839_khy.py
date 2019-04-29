sugarBag = int(input())

count5 = sugarBag//5 #5kg 짜리 갯수
rest5 = sugarBag%5 #나머지
bags = -1

#5키로그램짜리 봉지를 줄여가며 계산하기
for i in range(count5+1):
    if rest5 %3 == 0:
        count5 += rest5//3
        bags = count5
        break
    else:
        count5 -= 1
        rest5 = sugarBag - 5*count5

print(bags)