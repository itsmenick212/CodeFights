def higherVersion2(ver1, ver2):

    v1 = ver1.split('.')
    v2 = ver2.split('.')
    
    for i in range(len(v1)):
        if int(v1[i]) > int(v2[i]):
            return 1        
        elif int(v1[i]) > int(v2[i]):
            return -1
    
    return 0
