def pressingButtons(buttons):

    letters = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    
    def addLetters(b,r=[]):
        
        if not b:
            return r
        
        res = []
        l = list(letters[int(b[0])-2])
        if not r:
            res = l
            return addLetters(b[1:],res)
        
        for x in r:
            for s in l:
                res.append(x+s)
        
        return addLetters(b[1:],r=res)
    
    return addLetters(buttons)
