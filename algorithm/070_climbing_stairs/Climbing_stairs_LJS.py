def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    temp1 = 1
    temp2 = 2
    for i in range(2, n):
        result = temp2 + temp1
        temp1 = temp2
        temp2 = result
    return result


# dp = [0] * (n + 1)
# dp[0] = 1
# dp[1] = 1
# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + dp[i - 2]
# return dp[n]