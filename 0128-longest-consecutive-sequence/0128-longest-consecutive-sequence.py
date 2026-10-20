class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        maximum=1
        current=1
        i=1
        nums=list(set(nums))
        n=len(nums)
        nums.sort()
        while i<n:
            if nums[i]==nums[i-1]+1:
                current+=1
                maximum=max(maximum,current)
            else:
                current=1
            i+=1
        return maximum