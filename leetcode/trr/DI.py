def numPermsDISequence(s):
    dp = [0] * (len(s) + 1)
    x = int(pow(10, 9) + 7)
    i, tem = 0, 0
    dp[0] = 1
    while i < len(s):

        if s[i] == 'D':
            for j in range(i, -1, -1):
                dp[j] += dp[j + 1]
                dp[j] %= x
            dp[i + 1] = 0

        else:
            for j in range(1, i + 2):
                dp[j], tem = dp[j - 1] + tem, dp[j]
                dp[j] %= x
            dp[0], tem = 0, 0
        i += 1
    ans = sum(dp) % x
    return ans


s = "II"
print(numPermsDISequence(s))