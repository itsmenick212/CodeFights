def nearestGreater(a):

    if not a:
        return []
    length = len(a)
    s1 = [[0,a[0]]]
    s2 = [[length-1,a[-1]]]
    r = [-1] * length
    
    
    for i in range(length):
        # check right side for greater
        while s1 and s1[-1][1] < a[i]:
            x = s1.pop()
            # replace old result if there is one
            if r[x[0]] == -1 or abs(x[0]-i) < abs(x[0]-r[x[0]]):
                r[x[0]] = i
        s1.append([i,a[i]])
        
        # check left side for greater
        j = length - i - 1
        while s2 and s2[-1][1] < a[j]:
            x = s2.pop()
            # replace old result if there is one
            if r[x[0]] == -1 or abs(x[0]-j) <= abs(x[0]-r[x[0]]):
                r[x[0]] = j
        s2.append([j,a[j]])

    return r
