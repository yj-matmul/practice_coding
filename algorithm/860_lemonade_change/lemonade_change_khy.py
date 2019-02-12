class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dp = [0, 0, 0] #돈통
        result = True

        for i in bills:

            if i == 5: #5달러를 받을 경우
                dp[0] += 1

            if i == 10: #10달러를 받을 경우
                dp[0] -= 1
                dp[1] += 1

                if dp[0] < 0:
                    result = False
                    break

            if i == 20: #20달러를 받을 경우
                dp[2] += 1
                if dp[1] > 0 and dp[0] > 0:
                    dp[1] -= 1
                    dp[0] -= 1
                elif dp[0] >= 3:
                    dp[0] -= 3
                else:
                    result = False
                    break

        return result