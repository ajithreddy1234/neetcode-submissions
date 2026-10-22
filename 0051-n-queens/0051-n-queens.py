class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board=[["." for i in range(n)] for i in range(n)]
        res=[]
        def check(r,c,board):
            row=r-1
            while row>=0:
                if board[row][c]=="Q":
                    return False
                row-=1
            row,col=r-1,c-1
            while row>=0 and col>=0:
                if board[row][col]=="Q":
                    return False
                row-=1
                col-=1
            row,col=r-1,c+1
            while row>=0 and col<n:
                if board[row][col]=="Q":
                    return False
                row-=1
                col+=1
            return True
        def backtrack(r):
            if r==n:
                ls=[]
                for i in range(r):
                    ls.append("".join(board[i]))
                res.append(ls)
                return
            for c in range(n):
                if check(r,c,board):
                    board[r][c]="Q"
                    backtrack(r+1)
                    board[r][c]="."
        backtrack(0)
        return res


        