class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        class DSU:
            def __init__(self,n):
                self.parent=[i for i in range(n)]
                self.size=[1]*n
            def find(self,x):
                if x!=self.parent[x]:
                    self.parent[x]=self.find(self.parent[x])
                return self.parent[x]
            def union(self,x,y):
                A=self.find(x)
                B=self.find(y)
                if A==B:
                    return False
                if self.size[A]<self.size[B]:
                    A,B=B,A
                self.parent[B]=A
                self.size[A]+=self.size[B]
                return True
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        d=DSU(n*n)
        visited=set()
        res=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    visited.add((i,j))
                    cur=i*n+j
                    for dx,dy in directions:
                        nx=dx+i
                        ny=dy+j
                        if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1 and (nx,ny) not in visited :
                            nei=nx*n+ny
                            d.union(cur,nei)
                    res=max(res,d.size[d.find(cur)])
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    roots=set()
                    for dx,dy in directions:
                        nx=dx+i
                        ny=dy+j
                        if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:
                            roots.add(d.find(nx*n+ny))
                    can=1
                    for ele in roots:
                        can+=d.size[ele]
                    res=max(res,can)
        return res




        