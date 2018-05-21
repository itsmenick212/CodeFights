def sumOfTwo(a, b, v):

    b.sort()
    
    
    def binarySearch(b,l,r,x):
        
        if l <= r:
            m = (l+r)//2
            
            if b[m] == x:
                return True
            elif b[m] < x:
                return binarySearch(b,m+1,r,x)
            else:
                return binarySearch(b,l,m-1,x)
        else:
            return False
        
    
    for x in a:
        if binarySearch(b,0,len(b)-1,v-x):
            return True
                
    return False
    
    
