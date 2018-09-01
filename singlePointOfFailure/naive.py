def singlePointOfFailure(connections):
    
    n = len(connections)
    edges = 0
    for i in range(n):
        for j in range(i,n):
            if connections[i][j] == 1:
                connections[i][j] = 0
                connections[j][i] = 0
                visited = set()
                if sum(connections[0]) > 0:
                    stack = [0]
                    visited.add(0)
                    while stack:
                        node = stack.pop()
                        for k in range(n):
                            if k not in visited and connections[node][k] == 1:
                                visited.add(k)
                                stack.append(k)
                
                if len(visited) < n:
                    edges += 1
        
                connections[i][j] = 1
                connections[j][i] = 1
            
    return edges
