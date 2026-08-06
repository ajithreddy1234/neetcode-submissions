class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for l in range(1,len(nums)):
            if nums[l-1]==nums[l]:
                return nums[l]
            
        