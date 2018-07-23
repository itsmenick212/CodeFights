#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    
    if not t:
        return True
    
    s1 = [t.left]
    s2 = [t.right]
    
    while s1:
        c1 = s1.pop()
        c2 = s2.pop()
        
        if not c1 and not c2:
            pass
        elif ((not c1) != (not c2)) or c1.value != c2.value:
            return False
        else:
            s1.append(c1.left)
            s1.append(c1.right)
            s2.append(c2.right)
            s2.append(c2.left)
        
    return True
        
    
