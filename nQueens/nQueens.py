def nQueens(n):

    s = [[x] for x in range(1,n+1)]
    r = []
    
    def validMoves(sol):
        col = len(sol) + 1
        moves = [x for x in range(1,n+1) if x not in sol]
        for i,x in enumerate(sol):
            s1 = x + (col - (i+1))
            s2 = x - (col - (i+1))
            if s1 in moves:
                moves.remove(s1) 
            if s2 in moves:
                moves.remove(s2)
        return moves
        
    
    while s:
        c = s.pop()
        
        if len(c) == n:
            r.append(c)
        
        for i in validMoves(c):
            # check if spot is valid
            s.append(c+[i])
    
    return r[::-1]
