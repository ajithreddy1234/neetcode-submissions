
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        class DSU:
            def __init__(self,n):
                self.parent=[i for i in range(n+1)]
                self.size=[1]*(n+1)
            def find(self,x):
                print(x)
                if self.parent[x]!=x:
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
        D=DSU(n)
        for u,v in edges:
            if not D.union(u,v):
                return [u,v]



        