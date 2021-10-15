def isMatch(s,p):
    s,p = '#'+s,'#'+p

    dp = [[False for i in range(len(p))] for j in range(len(s))]
    dp[0][0]=True

    for i in range(len(s)):
        for j in range(1,len(p)):
            if i==0:
                dp[i][j]=j>1 and p[j]=='*' and dp[i][j-2]
                continue
            if p[j]=='.' or p[j]==s[i]:
                dp[i][j]=dp[i-1][j-1]
            if p[j]=='*':
                dp[i][j] = dp[i-1][j] and (p[j-1]=='.' or p[j-1]==s[i]) or dp[i][j-2] and j>1
        print(dp[i])
    return dp[-1][-1]

s = "mississippi"
p = "mis*is*ip*."

print(isMatch(s,p))