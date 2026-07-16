class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(m:int):
            s=1
            cu=0
            for num in nums:
                cu+=num
                if cu>m:
                    s+=1
                    if s>k:
                        return False
                    cu=num
            return True
        l=max(nums)
        r=sum(nums)
        while l<r:
            mid=l+(r-l)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return l