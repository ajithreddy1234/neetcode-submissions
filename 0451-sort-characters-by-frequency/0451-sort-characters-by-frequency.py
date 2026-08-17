class Solution:
    def frequencySort(self, s: str) -> str:
        x=Counter(s)
        print(x)
        heap=[]
        for key,value in x.items():
            heapq.heappush(heap,(-value,key))
        final=""
        while heap:
            x=heapq.heappop(heap)
            for _ in range(-1*x[0]):
                final+=str(x[1])
        return final

        