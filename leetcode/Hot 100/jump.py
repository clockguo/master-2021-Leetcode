# def jump(nums):
#     dp = [10000]*len(nums)
#     dp[-1] = 0
#     for i in range(len(nums)-2,-1,-1):
#         right = min(i+nums[i],len(nums)-1)
#         while right>i:
#             dp[i] = min(dp[right]+1,dp[i])
#             right -=1
#     return dp[0]

# def jump(nums):
#     dp = [10000000]*len(nums)
#     dp[-1] = 0
#     for i in range(len(nums)-2,-1,-1):
#         right = min(i+nums[i],len(nums)-1)
#         dp[i] = min(dp[i:right+1])+1
#     return dp[0]

def minjump(arr):
    dp = [10000]*len(arr)
    dp[-1] = 0
    dic = {}
    for i in range(len(arr)-1,-1,-1):
        if arr[i] not in dic:
            dic[arr[i]]=i

    for i in range(len(arr)-2,0,-1):
        dp[i-1] = dp[dic[arr[i-1]]]+1
        dp[i] = min(dp[i+1]+1,dp[i-1]+1,dp[i])
        if dp[dic[arr[i]]] > dp[i]:
            dic[arr[i]]=i

    dp[0]=min(dp[1]+1,dp[0])
    return dp[0]

nums = [68,-94,-44,-18,-1,18,-87,29,-6,-87,-27,37,-57,7,18,68,-59,29,7,53,-27,-59,18,-1,18,-18,-59,-1,-18,-84,-20,7,7,-87,-18,-84,-20,-27]
print(minjump(nums))