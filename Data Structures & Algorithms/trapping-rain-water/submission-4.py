class Solution:
    def trap(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        le=nums[l]
        re=nums[r]
        water=0
        while l<r:
            if le<=re:
                l+=1
                le=max(nums[l],le)
                water+=(le-nums[l])
            else:
                r-=1
                re=max(nums[r],re)
                water+=(re-nums[r])

        return water