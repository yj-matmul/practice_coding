class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        count = 0
        now = 0
        dp = [0]
        for i in range(1, num + 1):
            if i == 2 ** count:
                dp.append(1)
                now = 2 ** count
                count += 1
            else:
                rest = i - now
                dp.append(dp[rest] + 1)

        return dp