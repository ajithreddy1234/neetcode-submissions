class Trie:
    def __init__(self):
        self.child={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=Trie()
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.child:
                cur.child[c]=Trie()
            cur=cur.child[c]
        cur.end=True
    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur=root
            for i in range(j,len(word)):
                c=word[i]
                if c==".":
                    for ch in cur.child.values():
                        if dfs(i+1,ch):
                            return True
                    return False
                else:
                    if c not in cur.child:
                        return False
                    cur=cur.child[c]
            return cur.end
                
        return dfs(0,self.root)
        
