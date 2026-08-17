class Solution:
    def frequencySort(self, s: str) -> str:
        x=Counter(s)
        print(x)
        heap=[]
        for key,value in x.items():
            heapq.heappush(heap,(-value,key))
        final=[]
        while heap:
            x=heapq.heappop(heap)
            final.append(x[1]*(-1*x[0]))
        return "".join(final)

        