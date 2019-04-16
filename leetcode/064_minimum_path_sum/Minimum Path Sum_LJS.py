def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    temp = list(grid)
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                pass
            elif i == 0 and j > 0:
                temp[i][j] = temp[i][j - 1] + temp[i][j]
            elif i > 0 and j == 0:
                temp[i][j] = temp[i - 1][j] + temp[i][j]
            else:
                temp[i][j] = min(temp[i - 1][j], temp[i][j - 1]) + temp[i][j]

    return temp[-1][-1]

    # m = len(grid)
    # print(m)
    # n = len(grid[0])
    # print(n)
    # temp = [0] * n
    # for i in range(m):
    #     temp[0] += grid[i][0]
    #     for j in range(1, n):
    #         temp[j] = (min(temp[j], temp[j - 1]) or temp[j - 1]) + grid[i][j]
    #
    # return temp[-1]

a= minPathSum([[1,3,1],[1,5,1]])
print(a)

