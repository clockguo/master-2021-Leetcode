def canJump(nums):
    dp = [False]*len(nums)
    dp[-1] = True
    tem = len(nums)-1
    for i in range(len(nums)-2,-1,-1):
        if nums[i]+i>=tem:
            tem = i
            dp[i] = True
    return dp[0]

nums = [3,2,1,0,4]
print(canJump(nums))
