class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxx=[]
        count=0
        for i in range(n-1):
            if prices[i]<prices[i+1]:
                maxx.append(max(prices[i+1:n])-prices[i])
                count+=1
            
        if count==0:
            return 0
        else:
            return max(maxx)
        

        