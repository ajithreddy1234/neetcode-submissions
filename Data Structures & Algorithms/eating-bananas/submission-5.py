class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(l: int) -> bool:
            k=h
            for i in range(len(piles)):
                if k<=0:
                    return False
                k-=math.ceil(piles[i]/l)
            if k>=0:
                return True 
            else:
                return False
        r=max(piles)
        l=1
        answer=r
        while l<=r:
            mid=l+(r-l)//2
            if check(mid):
                r=mid-1
                answer=mid
            else:
                l=mid+1
        return answer
            

        



        