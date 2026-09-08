class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dist=[[float("inf") for i in range(cols)] for o in range(rows)]
        dist[0][0]=grid[0][0]
        for i in range(rows):
            for j in range(cols):
                value1=float("inf")
                value2=float("inf")
                if i>0:
                    value1=dist[i-1][j]
                if j>0:
                    value2=dist[i][j-1]
                if value1==value2==float("inf"):
                    dist[i][j]=grid[i][j]
                    continue
                dist[i][j]=grid[i][j]+min(value1,value2)
        return dist[rows-1][cols-1]
        