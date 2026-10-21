class Solution:
    def findMaxConsecutiveOnes(self, dp: list[int]) -> int:
        ma=0
        for i in range(len(dp)):
            if dp[i]==0:
                continue
            if i>0:
                dp[i]+=dp[i-1]
            ma=max(dp[i],ma)
        return ma