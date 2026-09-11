class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[float("inf") for i in range(amount+1)]
        dp[amount]=0
        for i in range(n-1,-1,-1):
            for j in range(amount,-1,-1):
                no=dp[j]
                take=float("inf")
                if j+coins[i]<=amount:
                    take=1+dp[j+coins[i]]
                dp[j]=min(take,no)
        return dp[0] if dp[0]!=float("inf") else -1

