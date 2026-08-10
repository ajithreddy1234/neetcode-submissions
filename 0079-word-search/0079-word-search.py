class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        column=len(board[0])

        visit=set()
        def dfs(r,c,i):
            if (r<0 or c<0 or r>rows-1 or c>column-1 or board[r][c]!=word[i] or (r,c) in visit):
                return False
            if i==len(word)-1:
                return True
            visit.add((r,c))
            found=(dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            visit.remove((r,c))
            return found
        for i in range(rows):
            for j in range(column):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False

        