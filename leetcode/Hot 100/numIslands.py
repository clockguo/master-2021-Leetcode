def numIslands(grid):
    def DFS(m, n):
        if grid[m][n] == '1':
            grid[m][n] = '2'
        else:
            return
        if 0 < m:
            DFS(m - 1, n)
        if m < len(grid) - 1:
            DFS(m + 1, n)
        if 0 < n:
            DFS(m, n - 1)
        if n < len(grid[0]) - 1:
            DFS(m, n + 1)

    count = 0
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[m][n] == '1':
                DFS(m, n)
                count += 1
    return count

grid = [
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]

print(numIslands(grid))