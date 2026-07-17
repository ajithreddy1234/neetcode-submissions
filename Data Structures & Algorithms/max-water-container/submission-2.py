class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=0
        while l<r:
            area=(r-l)*min(nums[l],nums[r])
            res=max(area,res)
            if nums[r]>nums[l]:
                l+=1
            else:
                r-=1
        return res