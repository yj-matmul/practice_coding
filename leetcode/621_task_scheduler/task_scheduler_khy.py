class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dp = {}
        if n >= 1:

            for i in tasks:
                if i in dp:
                    dp[i] += 1
                else:
                    dp[i] = 1

            dp_values = list(dp.values())
            dp_values.sort()
            max_dp = dp_values[-1]

            if (len(dp_values) > 1) and (dp_values[-1] - dp_values[-2]) >= n and (len(tasks) - max_dp) > (max_dp * n):
                return len(tasks)

            else:
                count = 0
                for k in dp_values[:-1]:
                    if k == max_dp:
                        count += 1

                print(max_dp, count)
                return max_dp + n * (max_dp - 1) + count

        else:
            return len(tasks)