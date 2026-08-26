class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        adj=defaultdict(list)
        for a,b in prerequisites:
            indegree[a]+=1
            adj[b].append(a)
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
        return topo if len(topo)==numCourses else []


        