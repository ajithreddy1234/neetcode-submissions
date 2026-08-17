import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        res=float("inf")
        running_res=0
        mg=(0,0)
        for r in range(len(arr)):
            running_res+=abs(arr[r]-x)
            if r-l+1==k:
                if running_res<res:
                    mg=(l,r)
                    res=running_res
                running_res-=abs(arr[l]-x)
                l+=1
        return arr[mg[0]:mg[1]+1]



