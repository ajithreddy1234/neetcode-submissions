class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        dp=nums[:]
        ma=0
        for i in range(len(nums)):
            if dp[i]==0:
                continue
            if i>0:
                dp[i]+=dp[i-1]
            ma=max(dp[i],ma)
        return ma