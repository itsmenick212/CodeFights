import heapq

def kthLargestElement(nums, k):
    
    nums = [-x for x in nums]
    heapq.heapify(nums)
    for _ in range(k-1):
        heapq.heappop(nums)
    return -heapq.heappop(nums)
