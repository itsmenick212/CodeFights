def sortByString(s, t):

    d1 = {}
    d2 = {}
    for i in range(len(t)):
        d1[t[i]] = i
        d2[i] =t[i] 
    
    l = []
    for x in s:
        l.append(d1[x])
    
    string = ''
    for x in sorted(l):
        string += d2[x]

    return string
