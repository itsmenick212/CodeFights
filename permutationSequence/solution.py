import math

def permutationSequence(n, k):
    
    k = k-1
    chars = [x for x in range(1,n+1)]

    r = ''
        
    for i in range(n):
        c = 0
        if len(chars) > 1:
            f = math.factorial(n-i-1)
            c = int(k/f)
            k -= c * f
        r += str(chars.pop(c))
        
    return r
