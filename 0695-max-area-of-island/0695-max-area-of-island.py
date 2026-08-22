class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count=0
        rows=len(grid)
        cols=len(grid[0])
        res=0
        def dfs(i,j):
            nonlocal count
            if i<0 or j<0 or i>rows-1 or j>cols-1 or grid[i][j]==0:
                return
            grid[i][j]=0
            count+=1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    count=0
                    dfs(i,j)
                    res=max(res,count)
        return res
            
        