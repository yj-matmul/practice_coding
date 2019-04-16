class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # 한 문자행의 길이
        N = len(A[0])
        # keep할 column 개수를 담을 메모리
        dp = [1] * N

        # 뒤에서부터 순서 비교
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                # 비교하려는 알파벳 뒤의 알파벳과 순서 비교해서 keep 여부 판단
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1 + dp[j])

        return N - max(dp)
