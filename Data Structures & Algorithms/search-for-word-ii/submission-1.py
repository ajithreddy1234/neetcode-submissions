class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res=[]
        row=len(board)
        col=len(board[0])
        def dfs(r,c,i):
            if i==len(word):
                return True
            if(r<0 or c<0 or r>=row or c>=col or board[r][c]!=word[i] ):
                return False
            board[r][c]='*'
            m=(dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            board[r][c]=word[i]
            return m
        for word in words:
            f=False
            for r in range(row):
                if f:
                    break
                for c in range(col):
                    if board[r][c]!=word[0]:
                        continue
                    if dfs(r,c,0):
                        res.append(word)
                        f=True
                        break
        return res
            






        