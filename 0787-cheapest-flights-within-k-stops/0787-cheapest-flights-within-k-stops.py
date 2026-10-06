import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        adj = defaultdict(list)

        for u, v, w in flights:
            adj[u].append((v, w))

        heap = []
        heapq.heappush(heap, (0, src, 0))
        dist=[[float("inf") for i in range(k+2)] for i in range(n)]
        while heap:
            co, node, fl = heapq.heappop(heap)
            if fl > k:
                continue
            if dist[node][fl]<co:
                continue
            for nei, extra in adj[node]:
                new_cost = extra + co
                if dist[nei][fl+1]>new_cost:
                    heapq.heappush(heap, (new_cost, nei, fl + 1))
                    dist[nei][fl+1]=new_cost
        mark=min(dist[dst])
        return mark if mark!=float("inf") else -1
