def hasPathWithGivenSum(t, s):
    
    if not t: 
        return(s == 0)

    def traverse(t,s):
        
        if not t:
            return False
        
        is_leaf = not t.left and not t.right
        
        new_s = s-t.value
        
        if is_leaf:
            return new_s==0
        
        l = traverse(t.left, new_s)
        r = traverse(t.right, new_s)
        return (l or r)
    
    return traverse(t,s)
