class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]  # bits array (0은 바로 넣어줌)

        for n in range(1, num + 1):
            # memoization dp 방식 이용
            ans.append(ans[n // 2] + n % 2)

        return ans
