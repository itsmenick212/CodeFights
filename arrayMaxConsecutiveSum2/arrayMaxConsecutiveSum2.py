def arrayMaxConsecutiveSum2(inputArray):
    
    if len(inputArray) == 1:
        return inputArray[0]

    large = inputArray[0]
    s = max(0,inputArray[0])
    i = 1
    while i < len(inputArray):
        s = s + inputArray[i]
        if s > large:
            large = s
        if s < 0:
            s = 0
        i+=1
    
    return large
        
        
