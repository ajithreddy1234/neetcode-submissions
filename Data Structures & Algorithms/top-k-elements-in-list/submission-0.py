
from collections import Counter 
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        co=Counter(nums)
        heap=[]
        for i in co.keys():
            heapq.heappush(heap,(co[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        