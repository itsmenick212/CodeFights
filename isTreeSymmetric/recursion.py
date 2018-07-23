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

    def traverse(t1,t2):
        
        if not t1:
            return not t2
        if not t2:
            return not t1
        if t1.value != t2.value:
            return False
        
        a = traverse(t1.left, t2.right)
        b = traverse(t1.right, t2.left)
        return (a and b)
    
    return traverse(t.left,t.right)
        
        
