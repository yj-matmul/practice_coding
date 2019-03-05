stack = []
dp = []
check = 0
for idx, s in enumerate(S):

    if s == "(": #(인 경우
        stack.append((idx, s))

    else:
        if idx - stack[-1][0] == 1: #합인경우
            dp.append(1)
            stack.pop()

        else: #곱인경우
            lendp = (idx - stack[-1][0]) // 2 #연산할 길이 정해주기
            sums = sum(dp[-lendp:]) * 2 #곱연산
            dp[-lendp:] = [0] * lendp #dp에서 연산 완료된 값 리셋
            dp.append(sums) #연산된 값 넣어주기
            stack.pop()

return sum(dp)