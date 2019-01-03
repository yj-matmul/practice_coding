class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n이 1, 2인 경우
        if n < 3:
            answer = n
        else:
            # 1~n까지의 답을 담을 리스트
            memo = [1, 2]
            for i in range(2, n):
                # 부분으로 나눠 생각 f(n) = f(n-1) + f(n-2)
                memo.append(memo[-1] + memo[-2])
            answer = memo[-1]

        return answer
