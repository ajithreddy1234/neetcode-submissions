class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
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
                    A,B
                self.parent[B]=A
                self.size[A]+=self.size[B]
                return True
        n=len(points)
        some=[]
        for i in range(n):
            for j in range(i+1,n):
                some.append([i,j,abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])])
        some.sort(key=lambda x:x[2])
        d=DSU(n)
        cost=0
        count=0
        for u,v,w in some:
            print(u,v,w)
            if d.union(u,v):
                count+=1
                cost+=w
            if count>=n-1:
                return cost
        return cost


        