class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        fin=1
        l=0
        su=0
        for r in range(len(nums)):
            su+=nums[r]
            while l<r and nums[r]*(r-l+1)>su+k:
                su-=nums[l]
                l+=1
            fin=max(fin,r-l+1)
        return fin





        