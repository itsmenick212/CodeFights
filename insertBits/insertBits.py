def insertBits(n, a, b, k):
    
    n1 = (n >> b+1) << b+1
    n2 = n & 2**(a)-1
    n3 = (k << a)
    return n1 + n2 + n3
