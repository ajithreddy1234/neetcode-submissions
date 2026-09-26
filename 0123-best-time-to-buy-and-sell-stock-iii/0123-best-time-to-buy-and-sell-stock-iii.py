class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo={}
        def solve(i,j,k):
            if k<=0:
                return 0
            if i>=len(prices):
                return 0
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            if j==0:
                buy=-prices[i]+solve(i+1,1,k)
                no=solve(i+1,j,k)
                memo[(i,j,k)]=max(buy,no)
                return memo[(i,j,k)]
            else:
                sell=prices[i]+solve(i+1,0,k-1)
                no=solve(i+1,j,k)
                memo[(i,j,k)]=max(sell,no)
                return memo[(i,j,k)]
        return solve(0,0,2)
        