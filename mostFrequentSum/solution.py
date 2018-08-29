#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def mostFrequentSum(t):
    
    if not t:
        return []
    
    sum_hash = {}
    
    stack1 = [t]
    stack2 = []
    max_sum = 0
    
    while stack1:
        root = stack1.pop()
        if root.left:         
            stack1.append(root.left)
        if root.right:
            stack1.append(root.right)
        stack2.append(root)
    
    max_sum = 0
    while stack2:
        root = stack2.pop()
        if root.left:
            root.value += root.left.value
        if root.right:
            root.value += root.right.value
        if root.value in sum_hash:
            sum_hash[root.value] += 1
        else:
            sum_hash[root.value] = 1
        max_sum = max(max_sum,sum_hash[root.value])
        
    result = []

    for item in sum_hash:
        if sum_hash[item] == max_sum:
            result.append(item)
    
    return sorted(result)
    
            
        
    
    
