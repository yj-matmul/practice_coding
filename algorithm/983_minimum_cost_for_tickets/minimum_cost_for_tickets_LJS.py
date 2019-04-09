def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    dp = [0] * 366

    for d in range(366):
        if d not in days:
            # 전날 최소cost 그대로 가져오기
            dp[d] = dp[d - 1]
            continue

        # 1일,7일,30일 티켓 비교시 어느경우 최소 cost인지 dp에 입력
        dp[d] = min(dp[d - 1] + costs[0], dp[max(0, d - 7)] + costs[1], dp[max(0, d - 30)] + costs[2])

        # days는 sort되있으므로, days[-1] 이후 dp는 볼 필요가 없음
        if d == days[-1]:
            dp = dp[:d + 1]
            break

    return dp[-1]
