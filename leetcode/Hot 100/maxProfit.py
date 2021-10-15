def maxProfit(prices):
    if not prices: return 0
    dp = [[0, 0, 0] for _ in range(2)]
    dp[0][0] = -prices[0]
    for i in prices:
        dp[1][0] = max(dp[0][0], dp[0][2] - i)
        dp[1][1] = dp[0][0] + i
        dp[1][2] = max(dp[0][1], dp[0][2])
        dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]
    return max(dp[1][2], dp[1][1])

prices = [1,2,3,0,2]
print(maxProfit(prices))