class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        src=(0,0)
        n=len(grid)
        if n==1 and grid[0][0]==0:
            return 1
        target=(n-1,n-1)
        dist=[[-1 for _ in range(n)] for _ in range(n)]
        dq=deque([src])
        dist[0][0]=1
        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1
        while dq:
            x,y=dq.popleft()
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]:
                nx,ny=dx+x,y+dy
                if 0<=nx<=n-1 and 0<=ny<=n-1 and dist[nx][ny]==-1 and grid[nx][ny]==0:
                    dist[nx][ny]=dist[x][y]+1
                    dq.append((nx,ny))
                if (nx,ny)==target:
                    return dist[nx][ny]
        return -1

        