class Trie:
    def __init__(self):
        self.child={}
        self.end=False
    def insert(self,word:int):
        cur=self
        for c in word:
            if c not in cur.child:
                cur.child[c]=Trie()
            cur=cur.child[c]
        cur.end=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Trie()
        for word in words:
            root.insert(word)
        res=set()
        visit=set()
        row=len(board)
        cols=len(board[0])
        def dfs(r,c,node,x):
            if (r<0 or c<0 or r>=row or c>=cols or board[r][c] not in node.child or  (r,c) in visit):
                return 
            visit.add((r,c))
            node=node.child[board[r][c]]
            x+=board[r][c]
            if node.end:
                res.add(x)
            dfs(r+1,c,node,x)
            dfs(r-1,c,node,x)
            dfs(r,c+1,node,x)
            dfs(r,c-1,node,x)
            visit.remove((r,c))
        

        for r in range(row):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(res)
        