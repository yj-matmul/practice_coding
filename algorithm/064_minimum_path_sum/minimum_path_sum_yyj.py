class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for n in range(1, len(grid[0])):
            grid[0][n] += grid[0][n - 1]
        for m in range(1, len(grid)):
            grid[m][0] += grid[m - 1][0]
        for m in range(1, len(grid)):
            for n in range(1, len(grid[0])):
                if grid[m - 1][n] < grid[m][n - 1]:
                    grid[m][n] += grid[m - 1][n]
                else:
                    grid[m][n] += grid[m][n - 1]

        return grid[-1][-1]
