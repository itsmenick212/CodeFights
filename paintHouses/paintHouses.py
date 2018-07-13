def paintHouses(cost):
    
    dp = [cost[0]]
    i = 1
    while i < len(cost):
        red = cost[i][0] + min(dp[i-1][1],dp[i-1][2])
        blue = cost[i][1] + min(dp[i-1][0],dp[i-1][2])
        green = cost[i][2] + min(dp[i-1][1],dp[i-1][0])
        dp.append([red,blue,green])
        i += 1
        
    return min(dp[-1])
