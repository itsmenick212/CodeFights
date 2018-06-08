#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    
    c = t
    s = [c]
    r = []
    if not t:
        return []
    while len(s):
        x = s.pop(0)
        r.append(x.value) 
        if x.left:
            s.append(x.left)
        if x.right:
            s.append(x.right)   
            
    return r
        
        
    
    
    
        
