N = int(input())
answer = 0

# 5킬로그램 봉지 추가 가능 여부 확인
# 추가 불가능일시, 3킬로그램 봉지로 가능 여부 확인
# 불가능일시 '-1' 로 변환

while N > 0:
    if (N - 5) % 5 == (0 or 3) or (N - 5) % 3 == 0:
        N = N - 5
        answer += 1
        continue

    if N % 3 == 0:
        answer += N // 3
    else:
        answer = -1
    break

print(answer)
