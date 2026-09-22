class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def value(div):
            su=0
            for num in nums:
                su+=math.ceil(num/div)
                if su>threshold:
                    return False
            return su<=threshold
        l=1
        r=max(nums)
        while l<r:
            mid=(l+r)//2
            if value(mid):
                r=mid
            else:
                l=mid+1
        return l
            

        