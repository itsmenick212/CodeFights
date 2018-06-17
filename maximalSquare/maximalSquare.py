def maximalSquare(matrix,s=1):
    
    if not matrix:
        return 0
    
    m = len(matrix[0])
    n = len(matrix)
    
    if s == 1:
        is_zero = True
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    is_zero = False
                    break
            if not is_zero:
                break
        if is_zero:
            return 0
               
    is_square = False
    new_matrix = [[0]*(m-1) for _ in range(n-1)]
    
    for i in range(n-1):
        for j in range(m-1):
            if matrix[i][j] == matrix[i+1][j] == matrix[i][j+1] == matrix[i+1][j+1] == '1':
                new_matrix[i][j] = '1'
                is_square = True
    
    print(new_matrix,s,is_square)
    
    if is_square:
        return maximalSquare(new_matrix,s=s+1)
    return s**2
        
        
        
        
        
        
    
