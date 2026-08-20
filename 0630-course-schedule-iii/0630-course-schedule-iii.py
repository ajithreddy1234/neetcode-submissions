class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:(x[1],x[0]))
        heap=[]
        time=0
        res=len(heap)
        for d,l in courses:
            if time+d<=l:
                heapq.heappush(heap,-d)
                time+=d
                res=max(res,len(heap))
            elif d>l:
                continue
            elif heap[0]+d<0:
                x=heapq.heappop(heap)
                time+=x
                if time+d<l:
                    heapq.heappush(heap,-d)
                    time+=d
                    res=max(res,len(heap))
        return res
            
