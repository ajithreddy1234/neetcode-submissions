class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0):
                return 0
            m=1
            grid[r][c]=0
            m+=dfs(r-1,c)
            m+=dfs(r+1,c)
            m+=dfs(r,c-1)
            m+=dfs(r,c+1)
            return m
        x=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    x=max(dfs(r,c),x)
        return x
        