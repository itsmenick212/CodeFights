def bubbleSort(items):
    
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                is_sorted = False
    
    return items
            
        
