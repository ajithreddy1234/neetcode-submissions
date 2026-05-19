class Solution:
    def minEatingSpeed(self, Piles: List[int], h: int) -> int:
        l=1
        r=max(Piles)
        res=r
        while l<=r:
            total=0
            m=(l+r)//2
            for p in Piles:
                total+=math.ceil(float(p)/m)
            if total<=h:
                res=m
                r=m-1
            else:
                l=m+1
        return res


        
            


        


        