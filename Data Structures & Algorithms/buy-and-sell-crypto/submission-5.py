class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l=0
        su=0
        for r in range(1,len(nums)):
            if nums[r]<nums[l]:
                l=r
            else:
                su=max(su,nums[r]-nums[l])
        return su
        