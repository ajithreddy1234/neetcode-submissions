class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x=[]
        for i in points:
            dist=math.sqrt(i[0]**2+i[1]**2)
            heapq.heappush(x,(dist,i))
        return [heapq.heappop(x)[1] for m in range(k)]
            
        