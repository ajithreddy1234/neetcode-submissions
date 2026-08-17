import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=Counter(nums)
        heap=[]
        for key,value in x.items():
            heapq.heappush(heap,[value,key])
            if len(heap)>k:
                heapq.heappop(heap)
        return [heap[i][1] for i in range(len(heap))]