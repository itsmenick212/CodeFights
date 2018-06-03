def climbingStairs(n):
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    r = [1,2]
    for i in range(2,n):
        r.append(r[i-1] + r[i-2])
    
    return r[n-1]
