class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        rows=len(grid)
        cols=len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>rows-1 or j>cols-1 or grid[i][j]=="0":
                return
            grid[i][j]="0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        return count
        [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]

            