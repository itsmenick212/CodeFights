def nextLarger(a):
    
    s = [[0,a[0]]]
    r = [-1] * len(a)
    
    for i in range(1,len(a)):
        if s:
            while s and a[i] > s[-1][1]:
                r[s[-1][0]] = a[i]
                s.pop()
        s.append([i,a[i]])
            
    return r
            
                
                
    
    
        
    
