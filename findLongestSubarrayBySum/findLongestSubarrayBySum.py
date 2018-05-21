def findLongestSubarrayBySum(s, arr):

    i = 0
    j = 0
    k = 0
    a = [-1]
    while i < len(arr) and j < len(arr):
        k += arr[j] 
        if k == s and (a == [-1] or a[1]-a[0] < j-i):
            a = [i+1,j+1]
            j += 1
        elif k <= s:
            j += 1
        else:
            k -= arr[i]
            k -= arr[j]
            i += 1
            
    return a
