class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1 for i in range(2)] for i in range(n)]
        def solve(i,j):
            if i>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if j==0:
                buy=-prices[i]+solve(i+1,1)
                no=solve(i+1,j)
                dp[i][j]=max(buy,no)
                return dp[i][j]
            else:
                sell=(prices[i]-fee)+solve(i+1,0)
                no=solve(i+1,j)
                dp[i][j]=max(sell,no)
                return dp[i][j]
        return solve(0,0)
        