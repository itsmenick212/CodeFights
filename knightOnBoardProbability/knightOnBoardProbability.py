import heapq

def knightOnBoardProbability(n, m, steps, x, y):

    heap = [steps*100 + x * 10 + y]
    cache = {}
    r = 1
    
    def findMoves(num):
        substep = int(num/100) - 1
        i = 0
        if len(str(num)) > 1:
            i = int(str(num)[-2])
        j = int(str(num)[-1])
        res = [(i+2,j+1),(i+2,j-1),(i-2,j+1),(i-2,j-1),(i+1,j+2),(i+1,j-2),(i-1,j+2),(i-1,j-2)]
        r = []
        for a,b in res:
            if a < 0 or b < 0 or a > n-1 or b > m-1:
                pass
            else:
                r.append(substep*100 + a * 10 + b)
        return r
    
    
    
    while heap:
        c = heapq.heappop(heap)
        if c not in cache:
            heapq.heappush(heap,c)
            if c > 99:
                temp = findMoves(c)
                is_in_cache = True
                for item in temp:
                    is_in_cache = is_in_cache and (item in cache)
                if is_in_cache:
                    cache[c] = sum([cache[_] for _ in temp]) * .125
                else:
                    for item in temp:
                        heapq.heappush(heap,item)
            else:
                cache[c] = 1
        else:
            pass
        
    return cache[steps*100 + x * 10 + y]
