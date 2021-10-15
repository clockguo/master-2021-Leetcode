def ismatch(s,p):
    s,p = '#'+s,'#'+p
    dp = [[False for _ in range(len(p))]for _ in range(len(s))]
    dp[0][0] = True
    for m in range(len(s)):
        for n in range(1,len(p)):
            if m == 0 :
                dp[m][n] = p[n] == '*' and dp[m][n-1]
                continue
            if p[n] !='*':
                if p[n] in [s[m],'?']:
                    dp[m][n] = dp[m-1][n-1]
                else: dp[m][n] = False
            else:
                if n ==1: dp[m][n] = True
                else:
                    dp[m][n] = dp[m-1][n-1] or dp[m][n-1] or dp[m-1][n]
    return dp[-1][-1]

s = "aab"
p =  "c*a*b"
print(ismatch(s,p))