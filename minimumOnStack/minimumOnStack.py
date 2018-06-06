def minimumOnStack(operations):
    s = []
    r = []
    for x in operations:
        if x == 'min':
            r.append(s[-1][1])
        elif x == 'pop':
            s.pop()
        else:
            k = int(x[5:])
            if not s:
                t = (k,k)
            else:
                t = (k,min(k,s[-1][1]))
            s.append(t)

    return r
