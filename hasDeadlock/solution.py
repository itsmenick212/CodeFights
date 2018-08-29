def hasDeadlock(connections):
  
    # Kahn's Algorithm
    stack = []
    count = 0
    n_edges = [0] * len(connections)
    
    for i in range(len(connections)):
        for j in connections[i]:
            n_edges[j] += 1
    
    for i in range(len(n_edges)):
        if n_edges[i] == 0:
            stack.append(i)
    
    if not stack:
        return True
    
    
    while stack:
        count += 1
        n = stack.pop()
        for m in connections[n]:
            n_edges[m] -= 1
            if n_edges[m] == 0:
                stack.append(m)
    
    return count != len(connections)
