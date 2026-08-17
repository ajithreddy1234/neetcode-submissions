class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        x=Counter(tasks)
        heap=[]
        for num in x.values():
            heapq.heappush(heap,-1*num)
        k=-1*heapq.heappop(heap)
        idle=(k-1)*n
        for _ in range(len(heap)):
            n=-1*heapq.heappop(heap)
            idle-=n
            if n==k:
                idle+=1
        return len(tasks)+(idle if idle>=0 else 0)
            
