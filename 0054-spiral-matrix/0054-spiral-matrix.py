class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        i=0
        j=0
        rows=len(matrix)
        cols=len(matrix[0])
        print(rows,cols)
        visited=set()
        final=[]
        def check(i,j):
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nx,ny=i+dx,j+dy
                    if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in visited:
                        return nx,ny
                return i,j
        while True:
            while j<cols and (i,j) not in visited:
                final.append(matrix[i][j])
                visited.add((i,j))
                j+=1
            j-=1
            i,j=check(i,j)
            if (i,j) in visited:
                return final
            while i<rows and (i,j) not in visited:
                final.append(matrix[i][j])
                visited.add((i,j))
                i+=1
            i-=1
            i,j=check(i,j)
            if (i,j) in visited:
                return final
            while j>=0 and (i,j) not in visited:
                final.append(matrix[i][j])
                visited.add((i,j))
                j-=1
            j+=1
            i,j=check(i,j)
            if (i,j) in visited:
                return final
            while i>=0 and (i,j) not in visited:
                final.append(matrix[i][j])
                visited.add((i,j))
                i-=1
            i+=1
            i,j=check(i,j)
            if (i,j) in visited:
                return final




            

