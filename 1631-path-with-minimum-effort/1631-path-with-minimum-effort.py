class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        dist=[[float("inf") for _ in range(cols)] for _ in range(rows)]
        heap=[(0,0,0)]
        dist[0][0]=0
        while heap:
            di,x,y=heapq.heappop(heap)
            if di>dist[x][y]:
                continue
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<=rows-1 and 0<=ny<=cols-1:
                    curr=abs(heights[nx][ny]-heights[x][y])
                    mg=max(curr,di)
                    if mg<dist[nx][ny]:
                        dist[nx][ny]=mg
                        heapq.heappush(heap,(mg,nx,ny))
        return dist[rows-1][cols-1]


            

        