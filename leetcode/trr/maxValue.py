def maxValue(grid):
    m,n = len(grid),len(grid[0])
    dp = [[0]*(n+1),[0]*(n+1)]
    i,j = 1, 1
    while i<=m:
        dp[1][0] = 0
        while j<=n:
            dp[1][j] = max(dp[0][j],dp[1][j-1])+grid[i-1][j-1]
            j +=1
        dp[0][1:] =dp[1][1:]
        j ,i= 1,i+1
    return dp[-1][-1]
grid = [[1,3,1],
  [1,5,1],
  [4,2,1]
]
grid = [[4]]
print(maxValue(grid))