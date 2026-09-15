class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[amount]=1
        for i in range(len(coins)-1,-1,-1):
            for j in range(amount,-1,-1):
                take=0
                if j+coins[i]<=amount:
                    take=dp[j+coins[i]]
                dp[j]=dp[j]+take
        return dp[0]

                
        
        