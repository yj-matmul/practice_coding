class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0

        # 숫자를 문자열로 변환해 연산
        s = str(x)

        # 부호가 있는 경우
        # 룰루랄라
        if s[0] == '-':
            # 끝 숫자가 0인 경우
            if s[-1] == 0:
                answer = -int(s[1:-1][::-1])
            else:
                answer = -int(s[1:][::-1])
        else:
            # 끝 숫자가 0인 경우
            if s[-1] == 0:
                answer = int(s[:-1][::-1])
            else:
                answer = int(s[::-1])

        # 32비트 표현을 넘어가는 경우
        if (answer >= 2 ** 31) or (answer < -2 ** 31): answer = 0

        return answer
