class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        dp1=[1]*n
        dp2=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    if dp1[i]<dp1[j]+1:
                        dp1[i]=dp1[j]+1
                        dp2[i]=dp2[j]
                    elif dp1[i]==dp1[j]+1:
                        dp2[i]+=dp2[j]
        ma=max(dp1)
        ans=0
        for i in range(n):
            if dp1[i]==ma:
                ans+=dp2[i]
        return ans

        