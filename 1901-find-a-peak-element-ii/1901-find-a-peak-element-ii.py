from collections import deque
class Solution:
    def findPeakGrid(self, mat):
        rows=len(mat)
        cols=len(mat[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        def check(i,j):
            for dx,dy in directions:
                nx=i+dx
                ny=i+dy
                if nx<0 or nx>=rows or ny<0 or ny>=cols:
                    continue
                if mat[nx][ny]>mat[i][j]:
                    return False
            return True
        dq=deque([(0,0),(rows-1,cols-1),(0,cols-1),(rows-1,0)])
        seen={((0,0),(rows-1,cols-1),(0,cols-1),(rows-1,0))}
        while dq:
            print(dq)
            i,j=dq.popleft()
            add=False
            for dx,dy in directions:
                nx=i+dx
                ny=j+dy
                if nx<0 or nx>=rows or ny<0 or ny>=cols:
                    continue
                if mat[nx][ny]>mat[i][j]:
                    print(nx,ny)
                    add=True
                    if (nx,ny) not in seen:
                        seen.add((nx,ny))
                        dq.append((nx,ny))
            if not add and check(i,j):
                return [i,j]
        return [-1,-1]