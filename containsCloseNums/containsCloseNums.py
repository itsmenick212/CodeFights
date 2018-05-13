def containsCloseNums(nums, k):

    d = {}
    for i,n in enumerate(nums):
        if n not in d:
            d[n] = [i]
        else:
            if i - d[n][-1] <=k:
                return True
            else:
                d[n].append(i)
    
    return False
