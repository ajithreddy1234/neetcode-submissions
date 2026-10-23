class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        di=[(1,0),(0,1),(-1,0),(0,-1)]
        dq=deque()
        rows=len(grid)
        cols=len(grid[0])
        yes=True
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    dq.append([i,j])
                    grid[i][j]=0
                if grid[i][j]==1:
                    yes=False
        if yes:
            return 0
        time=-1
        while dq:  
 
            lg=len(dq)    
            for i in range(lg):
                r,c=dq.popleft()
                for dr,dc in di:
                    nr=r+dr
                    nc=c+dc
                    if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]==0:
                        continue
                    change=True
                    grid[nr][nc]=0
                    dq.append([nr,nc])
            time+=1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return -1
        return time