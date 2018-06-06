def simplifyPath(path):

    path = path.split('/')
    r = []
    for p in path:
        if p == '..' and r:
            r.pop()
        elif p and not p == '.' and not p == '..':
            r.append(p)
        
    return '/' + '/'.join(r)
