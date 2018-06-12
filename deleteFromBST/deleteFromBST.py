#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def deleteFromBST(t, queries):

    def findX(r,x):
        parentNode = None
        curNode = r
        while curNode:
            if curNode.value == x:
                return parentNode, curNode
            elif x > curNode.value:
                parentNode = curNode
                curNode = curNode.right
            else:
                parentNode = curNode
                curNode = curNode.left
        return None, None
    
    def findRightMost(c):
        curNode = c
        while curNode.right:
            curNode = curNode.right
        return curNode
    
    def removeNode(p,x):
        p = parentNode
        if parentNode.right and parentNode.right.value == x:
            parentNode.right = None
        if parentNode.left and parentNode.left.value == x:
            parentNode.left = None

    def removeRight(node):
        if node.right:
            node.right = removeRight(node.right)
        else:
            return(node.left)
        return(node)
    
    for q in queries:
        parentNode, curNode = findX(t,q)
        if curNode:
            if curNode.left:
                rightMost = findRightMost(curNode.left)
                curNode.value = rightMost.value
                curNode.left = removeRight(curNode.left)
            elif curNode.right:
                curNode.value = curNode.right.value
                curNode.left = curNode.right.left
                curNode.right = curNode.right.right
            else:
                if parentNode:
                    removeNode(parentNode,curNode.value)
                else:
                    t = None
    return t
                
