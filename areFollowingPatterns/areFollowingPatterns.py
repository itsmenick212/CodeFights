def areFollowingPatterns(strings, patterns):

    if len(strings) != len(patterns):
        return False
    
    d1 = {}
    d2 = {}
    for i in range(len(strings)):
        if strings[i] not in d1 and patterns[i] not in d2:
            d1[strings[i]] = patterns[i] 
            d2[patterns[i]] = strings[i] 
        elif strings[i] in d1 and patterns[i] not in d2:
            return False
        elif strings[i] not in d1 and patterns[i] in d2:
            return False
        
    return True
            
