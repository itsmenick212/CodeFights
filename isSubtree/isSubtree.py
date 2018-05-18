#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(t1, t2):
    
    if not t2:
        return True
    
    def check(a,b):
        if not a and not b:
                return True
        if a and b:
            if a.value != b.value:
                return False
            return check(a.left,b.left) and check(a.right,b.right)
            

    def traverse(t):
        if t:
            if check(t,t2):
                return True
            return traverse(t.left) or traverse(t.right)
        return False
    
    return traverse(t1)
