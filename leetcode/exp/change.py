# import numpy as np
# n = int(input())arr = list(map(int, input().split()))
#
# r = np.root(arr)
# print(r)



# n = int(input())
# len1,arr = [],[]
# for i in range(n):
#     len1.append(int(input()))
#     line = list(map(int, input().split()))
#     arr.append(line)
def ok(s):
    max1 = 0
    def childstr(s, i, j):
        while i >= 1 and j < len(s)-1 and s[i-1]>s[i] and s[j]<s[j+1]:
            i, j = i - 1, j + 1
        return j - i + 1
    for i in range(1,len(s)):

        tem = childstr(s,i,i)
        if max1 <tem:
            max1 = tem
    return max1
# ans = []
# for i in range(n):
#     ans.append(ok(arr[i]))
# for i in ans:
#     print(i-1)





def maximalSquare(matrix):
    if not matrix or len(matrix[0])==0: return 0
    dp = [[0]*len(matrix[0]) for _ in range(2)]
    for i in range(len(matrix[0])):
        if matrix[0][i] == 'M':
            dp[0][i] = 1

    if len(matrix)==1:
        return max(dp[0])
    row = 1
    ans = max(dp[0])
    while row < len(matrix):
        col = 0
        while col <len((matrix[0])):
            if col==0:
                if matrix[row][col]=='M':
                    dp[1][col] = 1
                else:
                    dp[1][col] = 0
            else:
                if matrix[row][col] =='M':
                    dp[1][col] = min(dp[1][col-1],dp[0][col],dp[0][col-1])+1
                else:
                    dp[1][col] = 0
            col +=1
        dp[0] = dp[1][:]
        ans = max(max(dp[1]),ans)
        row+=1
    return ans*ans

m,n = map(int, input().split())
len1,arr = [],[]
for i in range(m):
    line = list(input())
    arr.append(line)
print(maximalSquare(arr))
