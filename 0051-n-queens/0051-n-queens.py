class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=[["."]*n for _ in range(n)]
        col=set()
        diag=set()
        neg_diag=set()
        def backtrack(r):
            if r==n:
                ans.append(["".join(boar) for boar in board])
            for i in range(n):
                if i in col or r+i in diag or r-i in neg_diag:
                    continue
                board[r][i]="Q"
                col.add(i)
                diag.add(r+i)
                neg_diag.add(r-i)
                backtrack(r+1)
                board[r][i]="."
                col.remove(i)
                diag.remove(r+i)
                neg_diag.remove(r-i)

        backtrack(0)
        return ans