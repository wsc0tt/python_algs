class Solution(object):
    def maxProfit(self, prices):
        lowest = float('inf') # set lowest to infinity
        profit = 0

        for price in prices:
            # update minimum price if curr price is lower
            lowest = min(lowest, price)
            # calc profit if selling at curr price
            profit = max(profit, price - lowest)
        
        return profit

