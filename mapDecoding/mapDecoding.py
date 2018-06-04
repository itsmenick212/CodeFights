def mapDecoding(message):

    length = len(message)
    
    a,b,c = 0,1,0
    for i in range(length):
        n1 = int(message[i])
        n2 = int(message[i-1:i+1]) if i>0 else 0
        if n1 > 0:
            c = b
        if(n2 < 27 and n2 > 9):
            c += a
        a = b
        b = c 
        c = 0
    return b % 1000000007

            
