class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        class DSU:
            def __init__(self,n):
                self.parents=[i for i in range(n)]
                self.size=[1]*n
                self.parent=0
            def find(self,x):
                if self.parents[x]!=x:
                    self.parents[x]=self.find(self.parents[x])
                return self.parents[x]
            def union(self,x,y):
                A=self.find(x)
                B=self.find(y)
                if A==B:
                    return False
                if self.size[A]<self.size[B]:
                    A,B=B,A
                self.parents[B]=A
                self.size[A]+=self.size[B]
                if self.size[self.parent]<self.size[A]:
                    self.parent=A
                return True
        bad=0
        d=DSU(n)
        for u,v in connections:
            if not d.union(u,v):
                bad+=1
        mg=len(set(d.find(i) for i in range(n)))
        if mg-1<=bad:
            return mg-1
        else:
            return -1

        