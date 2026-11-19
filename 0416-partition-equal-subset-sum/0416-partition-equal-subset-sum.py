from functools import cache
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        x=sum(nums)
        if x%2!=0:
            return False
        target=x//2
        dp=[[None]*(target+1) for i in range(len(nums))]
        def solve(i,val):
            if val==target:
                return True
            if val>target:
                return False
            if i>=len(nums):
                return False
            if dp[i][val] is not None:
                return dp[i][val]
            no=solve(i+1,val)
            take=False
            if nums[i]+val<=target:
                take=solve(i+1,val+nums[i])
            dp[i][val]=no or take
            return dp[i][val]
        return solve(0,0)