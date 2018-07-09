def streamValidation(stream):

    i = 0
    k = 0
    while i < len(stream):
        n = stream[i]
        if k > 0: 
            if n >> 6 != 2:
                return False
            else:
                k -= 1
        else:
            if n >> 3 == int('11110',2):
                k = 3
            elif n >> 4 == int('1110',2):
                k = 2
            elif n >> 5 == int('110',2):
                k = 1
            elif n >> 7 != 0:
                return False
                
        i += 1
                
    return k == 0
        
        
