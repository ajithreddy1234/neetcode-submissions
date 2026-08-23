class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>rows-1 or j>cols-1 or grid[i][j]==0:
                return
            grid[i][j]=0
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            return
        for i in range(rows):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][cols-1]==1:
                dfs(i,cols-1)
        for j in range(cols):
            if grid[0][j]==1:
                dfs(0,j)
            if grid[rows-1][j]==1:
                dfs(rows-1,j)
        res=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    res+=1
        return res

        