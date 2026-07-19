class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        l=0
        yo={}
        ma=0
        for r in range(len(nums)):
            yo[nums[r]]=1+yo.get(nums[r],0)
            while yo[nums[r]]>1:
                yo[nums[l]]-=1
                l+=1
            ma=max(ma,r-l+1)
        return ma
