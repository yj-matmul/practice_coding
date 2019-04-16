def minSteps(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    if n > 1: dp[2] = 2
    if n > 2: dp[3] = 3
    for i in range(4, n + 1):
        # 짝수 case
        if i % 2 == 0:
            dp[i] = dp[int(i/2)] + 2
        else:
            j = i - 2
            # 최대 약수를 찾는 과정 (자기 자신 제외)
            while j > 1:
                if i % j == 0:
                    break
                # -1 이 아닌 이유는 홀수x홀수 일 경우에만 홀수가 나오기 때문
                j -= 2
            # 소수 case
            if j == 1:
                dp[i] = i
            # 소수 아닌 홀수 case
            else:
                dp[i] = dp[j] + i / j
    return int(dp[-1])

print(minSteps(999))
