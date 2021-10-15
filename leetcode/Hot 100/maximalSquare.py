def maximalSquare(matrix):
    if not matrix or len(matrix[0]) == 0: return 0
    dp = [[0] * len(matrix[0]) for _ in range(2)]
    for i in range(len(matrix[0])):
        dp[0][i] = int(matrix[0][i])
    if len(matrix) == 1:
        return max(dp[0])
    row = 1
    ans = max(dp[0])
    while row < len(matrix):
        col = 0
        while col < len((matrix[0])):
            if col == 0:
                dp[1][col] = int(matrix[row][col])
            else:
                if matrix[row][col] == '1':
                    dp[1][col] = min(dp[1][col - 1], dp[0][col], dp[0][col - 1]) + 1
                else:
                    dp[1][col] = 0
            col += 1
        dp[0] = dp[1][:]
        ans = max(max(dp[1]), ans)
        row += 1
    return ans * ans

# ma = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# ma = [["1"]]
ma = [["1","0"],["0","0"]]
print(maximalSquare(ma))



