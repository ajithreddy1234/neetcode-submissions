class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def rob(nums: list[int]) -> int:
            first=0
            second=0
            for i in range(len(nums)):
                second,first=first,max(second+nums[i],first)
            return max(second,first)
        return max(rob(nums[1:]),rob(nums[:-1]))
        