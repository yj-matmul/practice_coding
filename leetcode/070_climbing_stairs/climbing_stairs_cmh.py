n = 10
# answer의 초기값
answer = [1, 2]

# 1인경우 1을 리턴
if n == 1:
    answer = 1

# n번째 계단은 n-1 번째 계단의 경우의 수 + 1 step
#             n-2 번째 계단의 경우의 수 + 2 steps
# 따라서, n-1 번째 계단의 경우의 수 + n-2 번째 계단의 경우의 수
else:
    for x in range(n - 2):
        answer.append(answer[x] + answer[x + 1])
    answer = answer[-1]

print(answer)
