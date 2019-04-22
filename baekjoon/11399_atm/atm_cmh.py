# 변수 입력 받기
T = int(input())
atm = list(map(int, input().split()))

# 변수 설정
answer = 0
wait_t = 0

# 오름차순 정렬
atm.sort()

# 누적시간 wait_t을 answer 에 반복 더함
for i in atm:
    wait_t += i
    answer += wait_t

print(answer)
