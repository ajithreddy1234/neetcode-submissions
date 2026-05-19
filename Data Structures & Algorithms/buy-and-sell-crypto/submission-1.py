class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        res=0
        count=0
        for i in range(n-1):
            if prices[i]<prices[i+1]:
                res=max(max(prices[i+1:n])-prices[i],res)
                count+=1
            
        if count==0:
            return 0
        else:
            return res

        