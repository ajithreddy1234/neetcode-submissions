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
        max_flights=k+1
        dist=[[float("inf") for _ in range(n)] for _ in range(max_flights+1)]
        print(dist)
        for u, v, w in flights:
            adj[u].append((v, w))

        # heap: (cost, node, flights_used)
        heap = [(0, src, 0)]
        dist[0][src]=0
        while heap:
            cost, node, flights_used = heapq.heappop(heap)
            if cost>dist[flights_used][node]:
                continue
            if node == dst:
                return cost
            if flights_used == k + 1:
                continue
            for nei, weight in adj[node]:
                new_cost = cost + weight

                if new_cost<dist[flights_used+1][nei]:
                    dist[flights_used+1][nei]=new_cost
                    heapq.heappush(heap,(new_cost,nei,flights_used + 1))
        return -1