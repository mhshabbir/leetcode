class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
                      s
            [7,6,4,3,1]
             b

        """
        profit = 0
        sell = 0
        buy = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            
            profit = max(profit, prices[sell] - prices[buy])
            sell += 1
        
        return profit
