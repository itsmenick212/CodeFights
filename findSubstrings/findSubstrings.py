class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.terminal = False
        # here we store the children nodes of this node
        # the letter of the children are the key, and the
        # TrieNode object is the value
        self.children = {}
        
def findSubstrings(words, parts):
    
    def addLetter(r,p):
        curNode = r
        for c in p:
            if c not in curNode.children:
                curNode.children[c] = TrieNode(c)
            curNode = curNode.children[c]
        curNode.terminal = True
    
    root = TrieNode('')
    for p in parts:
        addLetter(root,p)
        
        
    for k in range(len(words)):
        w = words[k]
        length = 0
        index = -1
        for i in range(len(w)):
            curNode = root
            wordlen = len(w)
            curWord = ''
            j = i
            while j < wordlen and w[j] in curNode.children:
                curNode = curNode.children[w[j]]
                curWord = curWord + w[j]
                j+=1
                if curNode.terminal and len(curWord) > length:
                    length = len(curWord)
                    index = i
        if index > 0:
            words[k] = w[:index] + '[' + w[index:index+length] + ']' + w[index+length:]
        
    return words
                
        
    
    
    
    
            
