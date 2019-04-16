class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 길이가 0인 경우
        if not len(prices):
            answer = 0
        else:
            # 최대 이익을 담을 공간
            dp = [0] * len(prices)
            maxi, mini = prices[0], prices[0]

            for n in range(len(prices)):
                # 최소값이 갱신되면 최대값 초기화
                if prices[n] < mini:
                    mini = prices[n]
                    maxi = prices[n]
                # 최대값 갱신
                if prices[n] > maxi:
                    maxi = prices[n]
                # 각 위치마다 최대 최소 담음
                dp[n] = maxi - mini
            answer = max(dp)

        return answer
