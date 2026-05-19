class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        res=0
        i=0
        while(i<n-1):
            if prices[i]<prices[i+1]:
                res=max(max(prices[i+1:n])-prices[i],res)
            i+=1

        return res

        