class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                if not j:
                    A[i][j] += min(A[i - 1][j], A[i - 1][j + 1])
                elif j == len(A[0]) - 1:
                    A[i][j] += min(A[i - 1][j - 1], A[i - 1][j])
                else:
                    A[i][j] += min(A[i - 1][j - 1], A[i - 1][j], A[i - 1][j + 1])

        return min(A[-1])
