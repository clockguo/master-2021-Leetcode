def getMaxMatrix(matrix):
    m, n = len(matrix),len(matrix[0])
    dp, ans= [0 for _ in range(n+1)],[0,0,0,0]
    max1 = matrix[0][0]
    for i in range(m):
        tem = [0]*n
        for j in range(i,m):

            for k in range(n):
                tem[k] +=matrix[j][k]
                dp[k+1] = max(dp[k]+tem[k],tem[k])
                if dp[k+1] == tem[k]:
                    begin = k

                if dp[k+1]>max1:
                    max1 = dp[k+1]
                    ans[0],ans[1],ans[2],ans[-1] = i,begin,j,k

    return ans


matrix = [[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]]

print(getMaxMatrix(matrix))
