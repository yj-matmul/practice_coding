def minFallingPathSum(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """

    for i in range(1, len(A), 1):
        for j in range(len(A[i])):
            if j == 0:
                A[i][j] = A[i][j] + min(A[i - 1][j], A[i - 1][j + 1])

            elif j == len(A[i]) - 1:
                A[i][j] = A[i][j] + min(A[i - 1][j - 1], A[i - 1][j])

            else:
                A[i][j] = A[i][j] + min(A[i - 1][j - 1], A[i - 1][j], A[i - 1][j + 1])

    return min(A[-1])

A = [[1,2,3],[4,5,6],[7,8,9]]
print(minFallingPathSum(A))
