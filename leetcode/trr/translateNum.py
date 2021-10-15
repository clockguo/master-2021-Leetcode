def translateNum(num):
    n = str(num)
    x = len(n)
    dp = [1] * (x + 1)

    i = 2
    while i <= x:
        x1 = n[i - 2] + n[i - 1]
        print(x1,'xxxx')
        if 10 <= int(n[i - 2] + n[i - 1]) <= 25:
            dp[i] = dp[i - 1] + dp[i-2]
        else:
            dp[i] = dp[i - 1]
        i += 1

    return dp[-1]

print(translateNum(25155))
