class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n=len(stones)
        total=sum(stones)
        dp=[0 for i in range(total+1)]
        for cur in range(total+1):
            dp[cur]=abs(total-2*cur)
        for i in range(n-1,-1,-1):
            cu=[0 for i in range(total+1)]
            for j in range(total+1):
                no=dp[j]
                take=float("inf")
                if stones[i]+j<=total:
                    take=dp[j+stones[i]]
                cu[j]=min(no,take)
            dp=cu
        return dp[0]