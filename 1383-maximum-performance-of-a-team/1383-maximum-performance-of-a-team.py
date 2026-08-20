import heapq
from typing import List

class Solution:
    def maxPerformance(
        self,
        n: int,
        speed: List[int],
        efficiency: List[int],
        k: int
    ) -> int:

        mod = 10**9 + 7

        x = []

        for i in range(n):
            x.append([efficiency[i], speed[i]])

        x.sort(reverse=True)

        cu = 0
        heap = []
        manage = 0

        for e, s in x:

            if len(heap) == k:

                # first include current engineer
                cu += s
                heapq.heappush(heap, (s, e))

                # remove smallest speed
                smallest_speed, old_efficiency = heapq.heappop(heap)
                cu -= smallest_speed

                # current e is the minimum efficiency
                res = cu * e
                manage = max(manage, res)

            else:

                cu += s
                heapq.heappush(heap, (s, e))

                res = cu * e
                manage = max(manage, res)

        return manage % mod