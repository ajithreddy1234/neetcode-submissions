class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
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
                return True
        n=len(s)
        d=DSU(n)
        for u,v in pairs:
            d.union(u,v)
        check=defaultdict(list)
        for i in range(n):
            check[d.find(i)].append(i)
        m=list(s)
        for key,value in check.items():
            l=sorted([m[ele] for ele in value])
            i=0
            for ele in value:
                m[ele]=l[i]
                i+=1
        print(m)
        return "".join(m)