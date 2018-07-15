def kpalindrome(s, k):
    
    dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
    
    for i in range(len(s)+1):
        for j in range(len(s)+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s[i-1] == s[-j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + 1
    
    return dp[-1][-1]/2 <= k
