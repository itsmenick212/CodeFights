def composeRanges(nums):
    
    r = []
    if nums:
        a = nums[0]
    else:
        return []
    
    length = len(nums)
    i = 0
    while i < length:
        if nums[i-1] + 1 < nums[i]:
            if nums[i-1] != a:
                r.append(str(a)+'->'+str(nums[i-1]))
            else:
                r.append(str(a))
            a = nums[i]
        i+=1
    
    if a == nums[-1]:
        r.append(str(a))
    else:
        r.append(str(a)+'->'+str(nums[-1]))
        
    return r
