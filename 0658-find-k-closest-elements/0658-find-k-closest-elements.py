class Pair():
    def __init__(self,val,x):
        self.val=val
        self.x=x
    def __lt__(self,other):
        return abs(self.val-self.x)>abs(other.val-self.x) or (abs(self.val-self.x)==abs(other.val-self.x) and self.val>other.val)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for val in arr:
            heapq.heappush(heap,Pair(val,x))
            if len(heap)>k:
                heapq.heappop(heap)
        return sorted([m.val for m in heap])