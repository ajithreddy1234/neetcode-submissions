class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        dq=deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    dq.append((i,j))
        visited=set()
        count=0
        while dq:
            for i in range(len(dq)):
                x,y=dq.popleft()
                if x<0 or y<0 or x>rows-1 or y>cols-1 or (x,y) in visited:
                    continue
                mat[x][y]=count
                visited.add((x,y))
                dq.append((x+1,y))
                dq.append((x-1,y))
                dq.append((x,y+1))
                dq.append((x,y-1))
            count+=1
        return mat
                          