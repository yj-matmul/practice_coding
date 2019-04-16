grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

m = len(grid)
n = len(grid[0])

for x in range(n - 1):
    grid[0][x+1] = grid[0][x] + grid[0][x+1]

for y in range(m -1):
    grid[y+1][0] = grid[y][0] + grid[y+1][0]

for x in range(1, m, 1):
    for y in range(1, n, 1):
        if grid[x][y-1] <= grid[x-1][y]:
            grid[x][y] = grid[x][y] + grid[x][y-1]
        else:
            grid[x][y] = grid[x][y] + grid[x-1][y]

print(grid[-1][-1])
