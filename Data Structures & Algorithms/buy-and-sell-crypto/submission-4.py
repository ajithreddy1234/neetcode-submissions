class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Track the lowest buying price seen so far
        max_profit = 0            # Track the maximum profit achieved
        
        for price in prices:
            # Update min_price if the current price is lower
            if price < min_price:
                min_price = price
            # Otherwise, calculate profit and update max_profit if it's better
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit