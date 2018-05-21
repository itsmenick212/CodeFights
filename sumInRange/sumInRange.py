def sumInRange(nums, queries):
    
    # create sum array
    a = [0]
    for i in range(len(nums)):
        a.append(a[i]+nums[i])
    
    o = 0
    for q in queries:
        o += a[q[1]+1] - a[q[0]]
    
    return o % (10**9 + 7)
