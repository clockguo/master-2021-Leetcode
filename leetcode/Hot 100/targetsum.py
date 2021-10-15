# def findTargetSumWays(nums, S):
#     dp = [[0]*(2*sum(nums)+1),[0]*(2*sum(nums)+1)]
#     dp[0][sum(nums)-nums[0]],dp[0][sum(nums)+nums[0]]=1,1
#     for i in range(1,len(nums)):
#         for j in range(len(dp[0])//2):
#             if j==0:
#                 dp[1][j],dp[1][-1] = dp[0][j+nums[i]],dp[0][-1-nums[i]]
#             else:
#                 dp[1][j],dp[1][-1-j] = dp[0][j-nums[i]]+dp[0][j+nums[i]],dp[0][-1-j+nums[i]]+dp[0][-1-j-nums[i]]
#         dp[1][len(dp[0])//2] = dp[0][len(dp[0])//2-1]+dp[0][len(dp[0])//2+1]
#         print(len(dp[0])//2)
#         dp[0]=dp[1][:]
#     return dp[0][S+sum(nums)]

def findTargetSumWays(nums, S):
    n = len(nums)
    suma = sum(nums)
    if abs(suma) < abs(S): return 0
    length = (2 * suma) + 1
    dp = [[0]*(2*sum(nums)+1),[0]*(2*sum(nums)+1)]
    dp[0][suma + nums[0]] = 1
    dp[0][suma - nums[0]] += 1
    for i in range(1, n):
        for j in range(length):
            l = dp[0][j - nums[i]] if 0 <= j - nums[i] < length else 0
            r = dp[0][j + nums[i]] if 0 <= j + nums[i] < length else 0
            dp[1][j] = l + r
        dp[0] = dp[1][:]
    return dp[0][suma + S]
nums = [1,0]
S = 1
print(findTargetSumWays(nums,S))