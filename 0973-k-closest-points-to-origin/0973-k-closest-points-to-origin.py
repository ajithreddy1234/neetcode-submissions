import math
class Pair:
    def __init__(self,coord):
        self.coord=coord
    def __lt__(self,other):
        return (self.coord[0]**2+self.coord[1]**2)>(other.coord[0]**2+other.coord[1]**2)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            heapq.heappush(heap,Pair(point))
            if len(heap)>k:
                heapq.heappop(heap)
        print(heap)
        return [p.coord for p in heap]

        