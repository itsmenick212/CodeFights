def permutationSequence(n, k):
    fac = [1]
    for i in xrange(1, n+1):
        fac.append(fac[-1] * i)
    
    people = range(1, n+1)
    ans = []
    k -= 1
    while k:
        q, r = divmod(k, fac[len(people)-1])
        ans.append(people.pop(q))
        k = r
    ans.extend(people)
    return "".join(map(str, ans))
