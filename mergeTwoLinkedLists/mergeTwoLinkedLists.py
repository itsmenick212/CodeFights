# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    
    if not l2:
        return l1
    if not l1:
        return l2
    
    if l1.value < l2.value :
        s = l1
        l1 = l1.next
    else:
        s = l2
        l2 = l2.next
        
    o = s
    while l1 or l2:
        if not l1:
            s.next = l2
            break
        if not l2:
            s.next = l1
            break
        if l1.value < l2.value:
            s.next = l1
            s = s.next
            l1 = l1.next
        elif l2.value <= l1.value:
            s.next = l2
            s = s.next
            l2 = l2.next
            
            
    return o
