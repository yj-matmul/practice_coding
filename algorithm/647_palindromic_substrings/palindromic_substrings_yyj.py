class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 문자열의 길이가 0일 경우
        if not len(s):
            answer = 0
        else:
            # 각 문자마다 회귀문 개수 담을 공간
            dp = [1] * len(s)

            for i in range(1, len(s)):
                for j in range(i - 1, -1, -1):
                    # 문자열이 대칭인지 체크
                    if s[j:i + 1] == s[j:i + 1][::-1]:
                        dp[i] += 1
            answer = sum(dp)

        return answer
