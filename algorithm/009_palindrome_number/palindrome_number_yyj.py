class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        answer = False
        # 숫자를 문자열로 변환
        s = str(x)

        # 문자열 길이에 따라 대칭 판단
        length = len(s)
        if length % 2:
            if s[:length // 2][::-1] == s[length // 2 + 1:]:
                answer = True
        else:
            if s[:length // 2][::-1] == s[length // 2:]:
                answer = True

        return answer
