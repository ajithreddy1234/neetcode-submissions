class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        dq=deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2: 
                    dq.append((i,j))  
        print(dq)
        if len(dq)>0:
            time=-1
        else:
            time=0
        while dq:
            for m in range(len(dq)):
                print(1)
                x,y=dq.popleft()
                if x<0 or y<0 or x>rows-1 or y>cols-1 or (x,y) in visited or grid[x][y]==0:
                    continue
                visited.add((x,y))
                if x+1>=0 and y>=0 and x+1<=rows-1 and y<=cols-1 and grid[x+1][y]==1:
                    dq.append((x+1,y))
                    grid[x+1][y]=2
                if x-1>=0 and y>=0 and x-1<=rows-1 and y<=cols-1 and grid[x-1][y]==1:
                    dq.append((x-1,y))
                    grid[x-1][y]=2
                if x>=0 and y+1>=0 and x<=rows-1 and y+1<=cols-1 and grid[x][y+1]==1:
                    dq.append((x,y+1))
                    grid[x][y+1]=2
                if x>=0 and y-1>=0 and x<=rows-1 and y-1<=cols-1 and grid[x][y-1]==1:
                    dq.append((x,y-1))
                    grid[x][y-1]=2
            time+=1
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    print(i,j)
                    count+=1
                    break
        return time if count==0 else -1
        

