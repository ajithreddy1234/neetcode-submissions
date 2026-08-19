from collections import Counter, deque

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap=[]
        for key,value in counter.items():
            heapq.heappush(heap,(-value,key))
        old_frq=0
        olf_key=""
        final=''
        while heap:
            x,y=heapq.heappop(heap)
            final+=y
            x+=1
            if old_frq<0:
                heapq.heappush(heap,(old_frq,olf_key))
            old_frq=x
            olf_key=y
        if old_frq<0:
            return ""
        return final
            
        