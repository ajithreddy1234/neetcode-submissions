from functools import cache
class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        x=sum(nums)
        if x%2!=0:
            return False
        target=x//2
        dp=[[False]*(target+1) for i in range(len(nums)+1)]
        dp[len(nums)][0]=True
        for i in range(len(nums)-1,-1,-1):
            for val in range(target+1):
                dp[i][val]=dp[i+1][val]
                if nums[i]<=val:
                    dp[i][val]=dp[i][val] or dp[i+1][val-nums[i]]
        return dp[0][target]
