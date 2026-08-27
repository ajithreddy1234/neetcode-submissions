class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows=len(maze)
        cols=len(maze[0])
        dist=[[-1 for _ in range(cols)]for _ in range(rows)]
        dist[entrance[0]][entrance[1]]=0
        dq=deque([entrance])
        while dq:
            x,y=dq.popleft()
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<=rows-1 and 0<=ny<=cols-1 and maze[nx][ny]=="." and dist[nx][ny]==-1:
                    print(nx,ny)
                    dist[nx][ny]=dist[x][y]+1
                    dq.append((nx,ny))
                    if nx==rows-1 or ny==cols-1 or nx==0 or ny==0:
                        return dist[nx][ny]
        return -1

        