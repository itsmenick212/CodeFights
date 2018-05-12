# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
    
def removeKFromList(l,k):
    if not l:
        return l
    
    while l and l.value == k:
        l = l.next
    

    m = l
    
    while m:
        t = m
        m = m.next
        while m and (m.value == k):
            m = m.next
        t.next = m
        
    return l
    

