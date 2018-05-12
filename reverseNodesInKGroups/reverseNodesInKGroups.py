# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverseNodesInKGroups(l, k):
	
    o = l
    c = l
    ahd2 = None
    while c:
        cnt = 0
        p = None
        ahd = c
        while cnt < k:
            n = c.next
            c.next = p
            p = c
            c = n
            cnt += 1
            if not c:
                break
        
        # if cnt was not completed, unreverse
        if cnt != k:
            c = p
            p = None
            for _ in range(cnt):
                n = c.next
                c.next = p
                p = c
                c = n
        
        # connect previous node to current node
        if ahd2:
        	ahd2.next = p
        else:
            o = p
        ahd2 = ahd
    
    return o
        
