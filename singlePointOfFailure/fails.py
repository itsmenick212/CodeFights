def singlePointOfFailure(connections):
    
    n = len(connections)
    visited = set([0])
    single_failure = set([x for x in range(n)])
    queue = [0]
    while queue:
        i = queue.pop(0)
        for j in range(n):
            if i == j:
                pass
            elif connections[i][j] == 1:
                if j not in visited:
                    queue.append(j)
                    visited.add(j)
                else:
                    if j in single_failure:
                        single_failure.remove(j)
                    if i in single_failure:
                        single_failure.remove(i)
                connections[i][j],connections[j][i] = 0,0
                    
    return len(single_failure)-1
