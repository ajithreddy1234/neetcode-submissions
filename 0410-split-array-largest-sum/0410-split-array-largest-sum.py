class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(m):
            spl=1
            su=0
            for num in nums:
                su+=num
                if su>m:
                    spl+=1
                    su=num
            return spl<=k
        l=max(nums)
        r=sum(nums)
        while l<r:
            m=(l+r)//2
            if check(m):
                r=m
            else:
                l=m+1
        return l


