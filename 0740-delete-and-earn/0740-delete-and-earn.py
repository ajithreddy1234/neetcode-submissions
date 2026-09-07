class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ma=max(nums)
        points=[0]*(ma+1)
        for num in nums:
            points[num]+=num
        dp=[0]*(ma+1)
        dp[0]=0
        if ma>=1:
            dp[1]=points[1]
        print(points)
        print(dp)
        for i in range(2,ma+1):
            dp[i]=max(dp[i-1],dp[i-2]+points[i])
        return dp[ma]


        