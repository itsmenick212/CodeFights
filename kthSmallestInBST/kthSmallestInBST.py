#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):
    
    global c
    global v
    c = 0
    v= 0

    def traverse(t):
        global c
        global v
        # if not left node, it is next smallest
        if t:
            traverse(t.left)
            c += 1
            if c == k:
                v = t.value
            return traverse(t.right)

    traverse(t)
    return v
