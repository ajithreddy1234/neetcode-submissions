class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dist=[[float("inf") for i in range(cols)] for o in range(rows)]
        dist[0][0]=grid[0][0]
        heap=[(grid[0][0],0,0)]
        while heap:
            weight,x,y=heapq.heappop(heap)
            if dist[x][y]<weight:
                continue
            for dx,dy in [(1,0),(0,1)]:
                nx=x+dx
                ny=y+dy
                if 0<=nx<rows and 0<=ny<cols and weight+grid[nx][ny]<dist[nx][ny]:
                    dist[nx][ny]=weight+grid[nx][ny]
                    heapq.heappush(heap,(weight+grid[nx][ny],nx,ny))
        return dist[rows-1][cols-1]
        