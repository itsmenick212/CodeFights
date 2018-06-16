import copy 

def wordBoggle(board, words):
    
    m = len(board)
    n = len(board[0])

    def isWordInBoard(b,w,t=None):
        if not w:
            return True
        first = w[0]
        if t==None:
            for i in range(m):
                for j in range(n):
                    # print(i,j,board[i][j])
                    if b[i][j] == first:
                        new_b = copy.deepcopy(b)
                        new_b[i][j]=''
                        if isWordInBoard(new_b,w[1:],t=(i,j)):
                            return True
        
        else:
            for i in range(t[0]-1,t[0]+2):
                for j in range(t[1]-1,t[1]+2):
                    if i>=0 and i<m and j>=0 and j<n and b[i][j] == first:
                        new_b = copy.deepcopy(b)
                        new_b[i][j]=''
                        if isWordInBoard(new_b,w[1:],t=(i,j)):
                            return True
                    
        return False
    
    r = []
    for w in words:
        if isWordInBoard(board,w):
            r.append(w)
            
    return sorted(r)
            
