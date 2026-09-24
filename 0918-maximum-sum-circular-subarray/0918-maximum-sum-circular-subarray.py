class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur=nums[0]
        mi=nums[0]
        total=nums[0]
        for num in nums[1:]:
            total+=num
            if cur>0:
                cur=num
            else:
                cur+=num
            mi=min(cur,mi)
        print(mi,total)
        cur=nums[0]
        ma=nums[0]
        for num in nums[1:]:
            if cur<0:
                cur=num
            else:
                cur+=num
            ma=max(cur,ma)
        if total==mi:
            return ma
        return max(ma,total-mi)

        

