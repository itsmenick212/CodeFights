# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    
    # reverse both lists
    c = a
    p = None
    alen = 0
    while c:
        n = c.next
        c.next = p
        p = c
        c = n
        alen += 1
    
    a = p
    
    c = b
    p = None
    blen = 0
    while c:
        n = c.next
        c.next = p
        p = c
        c = n
        blen += 1
    b = p
    
    s = 0
    if alen > blen:
        o = a
        p = b
        while a:
            if b:
                s = a.value + b.value + s
                if s > 9999:
                    a.value = s - 10000 
                    s = 1
                else:
                    a.value = s
                    s = 0
                b = b.next
            else:
                s = a.value + s
                if s > 9999:
                    a.value = s - 10000 
                    s = 1
                else:
                    a.value = s
                    s = 0
            if not a.next and s == 1:
                a.next = p
                p.value = 0
                p.next = None
            a = a.next
    else:
        o = b
        p = a
        while b:
            if a:
                s = a.value + b.value + s
                if s > 9999:
                    b.value = s - 10000 
                    s = 1
                else:
                    b.value = s
                    s = 0
                a = a.next
                
            else:
                s = b.value + s
                if s > 9999:
                    b.value = s - 10000 
                    s = 1
                else:
                    b.value = s
                    s = 0   
            if not b.next and s == 1:
                b.next = p
                p.value = 0
                p.next = None
            b = b.next
                
    
    c = o
    p = None
    while c:
        n = c.next
        c.next = p
        p = c
        c = n
    o = p
    return o
            
    
