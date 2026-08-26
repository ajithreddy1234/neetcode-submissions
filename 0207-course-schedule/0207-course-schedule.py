class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        adj=defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        dq=deque()
        for i in range(len(indegree)):
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
        return len(topo)==numCourses
        