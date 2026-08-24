class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dq=deque()
        zeros_exist=False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    dq.append((i,j))
                else:
                    zeros_exist=True
        visited=set()
        count=-1
        while dq:
            for i in range(len(dq)):
                x,y=dq.popleft()
                for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx = x + dx
                    ny=y+dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny]==0:
                        dq.append((nx,ny))
                        visited.add((nx,ny))
            count+=1

        return count if zeros_exist else -1
