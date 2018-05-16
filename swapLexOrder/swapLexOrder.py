def swapLexOrder(str, pairs):
    
    # sort pairs
    for p in pairs:
        if p[0] < p[1]:
            x = p[1]
            p[1] = p[0]
            p[0] = x
            
    pairs = sorted(pairs, reverse=True)
    
    # create hash of nodes
    d = {}
    d2 = {}
    for p in pairs:
        k = p[0]
        v = p[1]
        while v in d:
            v = d[v]
        while k in d:
            if d[k] > v:
                k = d[k]
                if k not in d and k > v:
                    d[k] = v
            elif d[k] < v:
                tmp = d[k]
                d[k] = v
                d[v] = tmp
            else:
                break
        d[k] = v
        
    
    # group numbers to head node
    for k in d:
        n = k
        v = d[k]
        while n in d:
            n = d[n]
        if n in d2:
            d2[n].append(k)
        else:
            d2[n] = [k]
    
    s = list(str)
    
    # create string
    for k in d2:
        l = sorted([k] + d2[k])
        tmp = []
        for i in l:
            tmp.append(s[i-1])
        tmp = sorted(tmp, reverse=True)
        count = 0
        for i in l:
            s[i-1] = tmp[count]
            count += 1
    

    s = ''.join(s)
    return s
