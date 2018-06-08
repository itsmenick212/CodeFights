#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def largestValuesInTreeRows(t):
    
    if not t:
        return []
    s = [[0,t]]
    r = []
    while s:
        i,x = s.pop(0)
        if len(r) <= i:
            r.append(x.value)
        else:
            r[i] = max(x.value,r[i])
        if x.left:
            s.append([i+1,x.left])        
        if x.right:
            s.append([i+1,x.right])
            
    return r
