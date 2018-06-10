#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#     
#     
def restoreBinaryTree(inorder, preorder):

    if not preorder:
        return None
    
    for i in range(len(preorder)):
        if preorder[i] in inorder:
            break
    if preorder[i] not in inorder:
        return None
    
    v = preorder[i]
    x = Tree(v)
    j = inorder.index(v)
    x.left = restoreBinaryTree(inorder[:j], preorder[i:])
    x.right = restoreBinaryTree(inorder[j+1:], preorder[i:])
    return x
