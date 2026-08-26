class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        reverse=[[] for _ in range(n)]
        outdegree=[0]*n
        for node in range(n):
            outdegree[node]=len(graph[node])
            for nei in graph[node]:
                reverse[nei].append(node)
        dq=deque()
        for i in range(len(outdegree)):
            if outdegree[i]==0:
                dq.append(i)
        topo=[]
        while dq:
            x=dq.popleft()
            topo.append(x)
            for nei in reverse[x]:
                outdegree[nei]-=1
                if outdegree[nei]==0:
                    dq.append(nei)
        return sorted(topo)




                
        