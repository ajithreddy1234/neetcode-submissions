class Solution:
    def highestPeak(self, iswater: List[List[int]]) -> List[List[int]]:
        rows=len(iswater)
        cols=len(iswater[0])
        dq=deque()
        visited=set()
        for i in range(rows):
            for j in range(cols):
                if iswater[i][j]==1:
                    dq.append((i,j))
                    visited.add((i,j))
        count=0  
        while dq:
            for i in range(len(dq)):
                x,y=dq.popleft()
                iswater[x][y]=count
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<=rows-1 and 0<=ny<=cols-1 and (nx,ny) not in visited:
                        dq.append((nx,ny))
                        visited.add((nx,ny))
            count+=1
        return iswater

