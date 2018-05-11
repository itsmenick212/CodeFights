# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):

    if l is None:
        return True
    
    f = l
    s = l
    while f.next:
        if f.next.next:   
            f = f.next.next
            s = s.next
        else:
            f = f.next
        
    # c is middle
    c = s.next
    p = None
    while c:
        n = c.next
        c.next = p
        p = c
        c = n
        
    s.next = p
    
    m = s.next
    
    while m:
        if m.value != l.value:
            return False
        m = m.next
        l = l.next
        
    return True
        
    
    
    
    
