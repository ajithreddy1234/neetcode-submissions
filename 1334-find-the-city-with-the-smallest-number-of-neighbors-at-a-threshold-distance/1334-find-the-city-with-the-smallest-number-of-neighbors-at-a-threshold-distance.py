class Solution:
    def findTheCity(self, V: int, edges: List[List[int]], distanceThreshold: int) -> int:
        fin = [set() for _ in range(V)]
        dist=[[float("inf") for _ in range(V)] for _ in range(V)]
        for i in range(V):
            dist[i][i]=0
        for u,v,w in edges:
            dist[u][v]=min(dist[u][v],w)
            dist[v][u]=min(dist[v][u],w)
        for k in range(V):
            for u in range(V):
                for v in range(V):
                    dist[u][v]=min(dist[u][k]+dist[k][v],dist[u][v])
                    if dist[u][v]<=distanceThreshold:
                        if u!=v:
                            fin[u].add(v)
                            fin[v].add(u)
        heap=[]
        for key,values in enumerate(fin):
            heapq.heappush(heap,(len(values),-key))
        return -heapq.heappop(heap)[1]

        