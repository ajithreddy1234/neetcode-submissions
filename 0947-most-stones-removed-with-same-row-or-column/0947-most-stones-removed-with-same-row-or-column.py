class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        class DSU:
            def __init__(self,n):
                self.parents=[i for i in range(n)]
                self.size=[1]*n
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
                return False
        n=len(stones)
        d=DSU(n)
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0]==stones[j][0] or stones[j][1]==stones[i][1]:
                    d.union(i,j) 
        print(d.parents)
        components=len(set([d.find(i) for i in range(n)]))
        return n-components           