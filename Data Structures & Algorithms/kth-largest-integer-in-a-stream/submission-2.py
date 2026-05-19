class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.minn=nums
        heapq.heapify(self.minn)
        while len(self.minn)>self.k:
            heapq.heappop(self.minn)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minn,val)
        if len(self.minn)>self.k:
            heapq.heappop(self.minn)
        return self.minn[0]
        
