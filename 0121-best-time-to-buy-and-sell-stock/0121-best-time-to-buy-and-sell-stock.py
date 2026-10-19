class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res=0
        mi=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<mi:
                mi=prices[i]
            res=max(prices[i]-mi,res)
        return res
        