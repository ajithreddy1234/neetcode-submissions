class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if m%2!=0:
                m=m-1
            if m+1<=len(nums)-1 and nums[m]==nums[m+1]:
                l=m+2
            else:
                r=m
        return nums[l]

        