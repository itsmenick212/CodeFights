def graphDistances(g, s):
    
    m = len(g)
    
    for k in range(m):
        for i in range(m):
            for j in range(m):
                if (g[i][j] < 0 or g[i][j] > g[i][k] + g[k][j]) and g[i][k]>=0 and g[k][j]>=0:
                    g[i][j] = g[i][k] + g[k][j]
    
    g[s][s] = 0
    
    return g[s]
