def countClouds(skyMap):
    
    r = 0
    if not skyMap:
        return r
    n = len(skyMap)
    m = len(skyMap[0])
    s = []
    
    def markX():
        while s:
            i,j = s.pop(0)
            skyMap[i][j] = 'X'
            # check all four borders
            if i+1 < n and skyMap[i+1][j] == '1':
                s.append((i+1,j))
            if i-1 >= 0 and skyMap[i-1][j] == '1':
                s.append((i-1,j))
            if j+1 < m and skyMap[i][j+1] == '1':
                s.append((i,j+1))
            if j-1 >= 0 and skyMap[i][j-1] == '1':
                s.append((i,j-1))
    
    for i in range(n):
        for j in range(m):
            if skyMap[i][j] == '1':
                r+=1
                s.append((i,j))
                markX()
    
    return r
                
