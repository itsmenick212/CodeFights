#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def digitTreeSum(t):

    s = [[0,t]]
    r = []
    while s:
        v,c = s.pop(0)
        if c.left:
            s.append([v*10+c.value,c.left])
        if c.right:
            s.append([v*10+c.value,c.right])
        if not c.left and not c.right:
            r.append(v*10+c.value)
    
    return sum(r)
        
        
