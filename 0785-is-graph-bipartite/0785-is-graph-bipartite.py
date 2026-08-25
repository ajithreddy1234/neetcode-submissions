class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[0]*n
        for i in range(n):
            if color[i]!=0:
                continue
            color[i]=1
            dq=deque([i])
            while dq:
                m=dq.pop()
                for nei in graph[m]:
                    if color[nei]==0:
                        color[nei]=-1*color[m]
                        dq.append(nei)
                    elif color[nei]==color[m]:
                        return False
        return True

        