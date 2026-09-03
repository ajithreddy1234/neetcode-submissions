class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        class DUS:
            def __init__(self,n):
                self.parent=[i for i in range(n)]
                self.size=[1]*n
            def find(self,x):
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
        d=DUS(n)
        adj=defaultdict(int)
        for i in range(n):
            for el in accounts[i][1:]:
                if el in adj:
                    print(i)
                    d.union(i,adj[el])
                else:
                    adj[el]=d.find(i)
        final=defaultdict(set)
        for j in range(n):
            for el in accounts[j][1:]:
                final[d.find(j)].add(el)
        print(final,d.parent)
        f=[]
        for key,elements in final.items():
            f.append([accounts[key][0]]+sorted(list(elements)))
        return f
        