def houseRobber(nums):
    
    length = len(nums)
    if not nums:
        return 0
    if length < 2:
        return max(nums)
    r = [nums[0], max(nums[:2])]
    for i in range(2,length):
        new = nums[i] + r[i-2] 
        if new > r[i-1]:
            r.append(new)
        else:
            r.append(r[i-1])
            
    return r[length-1]
