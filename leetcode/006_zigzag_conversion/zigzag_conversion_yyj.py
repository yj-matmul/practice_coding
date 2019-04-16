class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        answer = ""
        # 규칙성을 위해
        divisor = numRows * 2 - 2

        # numRows가 1인 경우를 대비
        if divisor == 0: divisor = 1

        q = len(s) // divisor

        for n in range(divisor // 2 + 1):
            for quo in range(q + 1):
                # 마지막 몫인 경우
                if quo == q:
                    if (n in [0, divisor / 2]) & (quo * divisor + n < len(s)):
                        answer += s[quo * divisor + n]
                    elif (quo * divisor + n < len(s)) & ((quo + 1) * divisor - n < len(s)):
                        answer += s[quo * divisor + n] + s[(quo + 1) * divisor - n]
                    elif quo * divisor + n < len(s):
                        answer += s[quo * divisor + n]
                else:
                    if n in [0, divisor // 2]:
                        answer += s[quo * divisor + n]
                    else:
                        answer += s[quo * divisor + n] + s[quo * divisor + divisor - n]

        return answer
