def twoSum(n):
    m = 6*n
    dp = [[0]*(m+1),[0]*(m+1)]

    for pp in range(1,7):
        dp[0][pp] = 1
    print(dp)
    for layer in range(1,n):
        j = layer+1
        print(layer)
        while j<=m:
            i = 1
            while i<=6:
                if j-i>0:
                    dp[1][j] +=dp[0][j-i]
                else: break
                i +=1
            j +=1
        dp[0] = dp[1]
        dp[1] = [0]*(m+1)
    for i in range(n, m + 1):
        dp[0][i] = dp[0][i]/pow(6,n)
    return dp



print(twoSum(1))