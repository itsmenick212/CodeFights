# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    
    if not l or n == 0:
        return l

	# reverse list first
    p = None
    end = l
    while l:
        nxt = l.next
        l.next = p
        p = l
        l = nxt
        
    l = p
    
    # keep track of original beginning node in case len(l) == k
    a = l
    
    mid = l
    for _ in range(n-1):
        l = l.next
        
    beg = l.next
    
    
    if beg:
        l.next = None
        end.next = mid
    # in n == len(l), just reverse
    else:
        beg = a
    
    # reverse list again
    p = None
    cur = beg
    while cur:
        nxt = cur.next
        cur.next = p
        p = cur
        cur = nxt
    
    
    return p
        
