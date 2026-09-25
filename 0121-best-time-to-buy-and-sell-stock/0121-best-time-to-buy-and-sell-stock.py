class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0  for i in range(2)] for i in range(len(nums)+1)]
        dp[n-1][1]=nums[n-1]
        for i in range(n-2,-1,-1):
            dp[i][0]=max(dp[i+1][1]-nums[i],dp[i+1][0])
            dp[i][1]=max(dp[i+1][1],nums[i])
        return dp[0][0]