def longestIncreasingSubsequence(s):

    dp = [1]
    
    for i in range(1,len(s)):
        n = s[i]
        c_max = 0
        for j in range(i):
            if n > s[j] and dp[j] > c_max:
                c_max = dp[j]
        dp.append(c_max + 1)
        
    return max(dp)
