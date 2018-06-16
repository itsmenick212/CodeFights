def combinationSum(a, n):
    
    a = sorted([x for x in set(a) if x <= n])
    s = [[x] for x in a]
    r = []
    
    while s:
        c = s.pop()
        sum_c = sum(c)
        if sum_c == n:
            r.append(c)
        else:
            for x in [x for x in a if x >= c[-1]]:
                if sum_c + x <= n:
                    s.append(c+[x])
    
    s = ''
    for l in r[::-1]:
        tmp = ''
        for e in l:
            tmp += str(e) + ' '
        tmp = tmp[:len(tmp)-1]
        s += '(' + tmp +')'
    
    if not s:
        return 'Empty'
    return s
