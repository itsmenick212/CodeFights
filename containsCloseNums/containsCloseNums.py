def containsCloseNums(nums, k):

    d = {}
    for i,n in enumerate(nums):
        if n not in d:
            d[n] = [i]
        else:
            d[n].append(i)
    
    for a in d:
        if len(d[a])>1:
            for i in range(len(d[a])-1):
                if d[a][i+1] - d[a][i] <= k:
                    return True
    
    return False
