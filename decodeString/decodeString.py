def decodeString(s):

    r = [[1,'']]
    for i in range(len(s)):
        if s[i].isdigit():
            if i>0 and s[i-1].isdigit():
                r[-1][0] = r[-1][0] * 10 + int(s[i])
            else:
                r.append([int(s[i]),''])

        elif s[i] == ']':
            t = r[-1][0] * r[-1][1]
            r.pop()
            r[-1][1] = r[-1][1] + t
        elif s[i] != '[':
            r[-1][1] = r[-1][1] + s[i]
    
    return r[0][1]
            
        
