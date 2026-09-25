class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0,nums[n-1]]
        for i in range(n-2,-1,-1):
            cu=[0,0]
            cu[0]=max(dp[1]-nums[i],dp[0])
            cu[1]=max(dp[1],nums[i])
            dp=cu
        return dp[0]