class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n=len(nums)
        dp=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j]%nums[i]==0:
                    dp[i]=max(dp[i],dp[j]+1)
        val=0
        for i in range(n):
            val=max(val,dp[i])
        fin=[]
        last=1
        for i in range(n):
            if dp[i]==val and nums[i]%last==0:
                fin.append(nums[i])
                val-=1
                last=nums[i]
        return fin

        