from heapq import heappush, heappop

def graphDistances(g, s):
    
    def djikstra(s,t):
        unvisited = set([x for x in range(len(g))])
        heap = [(0,s)]
        
        while heap:
            c = heappop(heap)
            if c[1] == t:
                return c[0]
            for i in unvisited:
                d = g[c[1]][i]
                if d >= 0:
                    heappush(heap, (d + c[0],i))
            if c[1] in unvisited:
                unvisited.remove(c[1])
                
        return None
    
    for i in [x for x in range(len(g)) if x is not s]:
        g[s][i] = djikstra(s,i)

    g[s][s] = 0

    return g[s]
