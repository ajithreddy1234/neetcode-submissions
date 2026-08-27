class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        dist=[float("inf")]*(n+1)
        for u,v,w in times:
            adj[u].append((v,w))
        dist[k]=0
        heap=[(0,k)]
        while heap:
            d,node=heapq.heappop(heap)
            if d>dist[node]:
                continue
            for nei,di in adj[node]:
                new_d=d+di
                if new_d<dist[nei]:
                    dist[nei]=new_d
                    heapq.heappush(heap,(new_d,nei))
        x=max(dist[1:])
        return x if x!=float("inf") else -1

        