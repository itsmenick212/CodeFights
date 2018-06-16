def sumSubsets(arr, num):
    
    s = [[i,[x]] for i,x in enumerate(arr) if x <= num]
    r = []
    length = len(arr)
    
    while s:
        i,c = s.pop()
        nsum = sum(c)
        if nsum == num and c not in r:
            r.append(c)
        else:
            for j in range(i+1,length):
                new_n = arr[j]
                if sum(c) + new_n <=num:
                    s.append([j,c+[new_n]])
    if not r:
        return [[]]
    return r[::-1]
