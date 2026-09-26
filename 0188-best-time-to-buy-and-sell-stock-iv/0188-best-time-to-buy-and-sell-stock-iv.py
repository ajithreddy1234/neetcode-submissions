class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n=len(prices)
        dp=[[[-1 for i in range(k+1)]for i in range(2)] for i in range(n)]
        def solve(i,j,k):
            if k<=0:
                return 0
            if i>=len(prices):
                return 0
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
            if j==0:
                buy=-prices[i]+solve(i+1,1,k)
                no=solve(i+1,j,k)
                dp[i][j][k]=max(buy,no)
                return dp[i][j][k]
            else:
                sell=prices[i]+solve(i+1,0,k-1)
                no=solve(i+1,j,k)
                dp[i][j][k]=max(sell,no)
                return dp[i][j][k]
        return solve(0,0,k)
        