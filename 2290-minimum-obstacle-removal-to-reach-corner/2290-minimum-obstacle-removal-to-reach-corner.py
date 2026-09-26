class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        if grid[0][0]==0:
            heap=[(0,0,0)]
        else:
            heap=[(1,0,0)]
        dist=[[float("inf") for i in range(cols)] for i in range(rows)]
        while heap:
            obst,x,y=heapq.heappop(heap)
            print(obst,x,y)
            if dist[x][y]<obst:
                continue
            for dx,dy in directions:
                nx=x+dx
                ny=y+dy
                if nx<0 or nx>=rows or ny<0 or ny>=cols:
                    continue
                if grid[nx][ny]==0:
                    if dist[nx][ny]>obst:
                        dist[nx][ny]=obst
                        heapq.heappush(heap,(obst,nx,ny))
                else:
                    if dist[nx][ny]>obst+1:
                        dist[nx][ny]=obst+1
                        heapq.heappush(heap,(obst+1,nx,ny))
        return dist[rows-1][cols-1]



        