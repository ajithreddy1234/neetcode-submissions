class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj=defaultdict(list)
        indegree=[0]*n
        for l,r in edges:
            adj[l].append(r)
            adj[r].append(l)
            indegree[l]+=1
            indegree[r]+=1
        dq=deque()
        for i in range(n):
            if indegree[i]==1:
                dq.append(i)
        rem=n
        while rem>2:
            size=len(dq)
            rem-=size
            for i in range(size):
                x=dq.popleft()
                for nei in adj[x]:
                    indegree[nei]-=1
                    if indegree[nei]==1:
                        dq.append(nei)
        return list(dq)




        