def regularExpressionMatching(s, p):
    dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
    dp[0][0] = True
    for j in range(1,len(p)):
        dp[0][j+1] = dp[0][j-1] and p[j] == '*'
    for i in range(len(s)):
        for j in range(len(p)):
            if p[j] == '*':
                if dp[i+1][j-1]:
                    dp[i+1][j+1] = True
                else:
                    dp[i+1][j+1] = (p[j-1] == s[i] or p[j-1] == '.') and dp[i][j+1]
            else:
                dp[i+1][j+1] = dp[i][j] and (p[j] == s[i] or p[j] == '.')
                
    return dp[-1][-1]
