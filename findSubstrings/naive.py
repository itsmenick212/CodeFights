def findSubstrings(words, parts):

    parts = sorted(parts,key=len,reverse=True)

    for i in range(len(words)):
        w = words[i]
        length = 0
        j = len(w)
        for p in parts:
            if p in w:
                if len(p) >= length and w.find(p) < j:
                    length = len(p)
                    j = w.find(p)
                elif len(p) < length:
                    break
        if length > 0:
            words[i] = w[:j] + '[' + w[j:j+length] + ']' + w[j+length:]
    
    return words
                

