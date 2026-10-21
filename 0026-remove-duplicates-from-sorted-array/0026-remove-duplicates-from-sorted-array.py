class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l=0
        for r in range(len(nums)):
            if r>0 and nums[r]==nums[r-1]:
                continue
            nums[l]=nums[r]
            l+=1
        return l