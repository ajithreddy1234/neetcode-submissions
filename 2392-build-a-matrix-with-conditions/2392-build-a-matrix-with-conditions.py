class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(condition):
            adj=defaultdict(list)
            indegree=[0]*(k+1)
            for u,v in condition:
                adj[u].append(v)
                indegree[v]+=1
            dq=deque()
            for i in range(1,k+1):
                if indegree[i]==0:
                    dq.append(i)
            topo=[]
            while dq:
                x=dq.popleft()
                topo.append(x)
                for nei in adj[x]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        dq.append(nei)
            if len(topo)!=k:
                print(0)
                return []
            return topo
        la=topo(rowConditions)
        y=topo(colConditions)
        if not la or not y:
            return []
        fina=defaultdict(list)
        for i in range(k):
            fina[la[i]].append(i)
        for j in range(k):
            fina[y[j]].append(j)
        submi=[[0 for _ in range(k)] for _ in range(k)]
        for m,n in fina.items():
            submi[n[0]][n[1]]=m
        return submi


        