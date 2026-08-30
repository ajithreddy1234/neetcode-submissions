class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dist=[[float("inf") for _ in range(cols)] for _ in range(rows)]
        dist[0][0]=grid[0][0]
        heap=[(grid[0][0],0,0)]
        time=0
        while heap:
            h,x,y=heapq.heappop(heap)
            print(h,x,y)
            if h>dist[x][y]:
                continue
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny=dx+x,dy+y
                if 0<=nx<rows and 0<=ny<cols:
                    update=max(grid[nx][ny],h)
                    if dist[nx][ny]>update:
                        dist[nx][ny]=update
                        heapq.heappush(heap,(update,nx,ny))
        return dist[rows-1][cols-1]

        