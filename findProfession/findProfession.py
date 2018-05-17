def findProfession(level, pos):
    
    def traverse(l,p,x):

        if l == 1:
            return x
        
        n = 2**(l-1)
        
        if p <= n/2:
            d = 'left'
        else:
            d = 'right'
            p = p - n/2
        
        if (x == 'Engineer' and d == 'left') or (x == 'Doctor' and d == 'right'):
            x = 'Engineer'
        else:
            x = 'Doctor'
        
        return traverse (l-1,p,x)
    
    return traverse (level,pos,'Engineer')
