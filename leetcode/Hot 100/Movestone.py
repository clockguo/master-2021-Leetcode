def moveStone(n,arr):
    dic, max1= {}, 0
    dp = [1]*n
    for i in range(n):
        if arr[i] not in dic:
            dic[arr[i]] = i
        if arr[i]-1 in dic:
            dp[i] = dp[dic[arr[i]-1]]+1
        if max1<dp[i]:
            max1 = dp[i]
    return n-max1

n = 6
arr =[2, 1,3, 4, 6, 5]
print(moveStone(n,arr))