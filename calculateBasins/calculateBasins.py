def calculateBasins(grid):

    m = len(grid)
    n = len(grid[0])
    
    sizes = {}
    meme = {}
    
    def search(i,j):
        sink = True
        minX, minY = i,j
        if i*200+j in meme:
            return meme[i*200+j]
        for x,y in [(0,-1),(0,1),(1,0),(-1,0)]:
            if i+x<m and i+x>=0 and j+y<n and j+y>=0:
                if grid[minX][minY] > grid[i+x][j+y]:
                    minX,minY = i+x,j+y
                    sink = False
        if sink:
            r = i*200+j
        else:
            r = search(minX,minY)
        meme[i*200+j] = r
        return r
    
    for i in range(m):
        for j in range(n):
            # for each element, find basin
            sink = search(i,j)
            if sink not in sizes:
                sizes[sink] = 0
            sizes[sink] += 1
            
    return sorted(sizes.values(),reverse=True)
