class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        r=[]
        c=[]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    r.append(i)
                    c.append(j)
        print(matrix)
        for i in range(len(r)):
            for j in range(cols):
                if r[i]<rows:
                    matrix[r[i]][j]=0
        print(matrix)
        for i in range(len(c)):
            for j in range(rows):
                if c[i]<cols:
                    matrix[j][c[i]]=0

        return matrix
        