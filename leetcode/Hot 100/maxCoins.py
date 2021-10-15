def maxCoins(nums):
    nums.insert(0,1)
    nums.append(1)
    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums)-1)]

    for i in range(len(nums)-3,-1,-1):
        for j in range(i+2,len(nums)):
            for k in range(i+1,j):
                dp[i][j] = max(dp[i][j],dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
    print(dp)
    return dp[0][-1]

nums = [3,1,5,8]
print(maxCoins(nums))
