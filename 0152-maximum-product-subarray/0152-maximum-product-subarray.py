class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[[0]*2 for i in range(n)]
        dp[0][0]=dp[0][1]=nums[0]
        ans=nums[0]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0]*nums[i],nums[i],dp[i-1][1]*nums[i])
            dp[i][1]=min(dp[i-1][0]*nums[i],nums[i],dp[i-1][1]*nums[i])
            ans=max(ans,dp[i][0])
        return ans

        
        