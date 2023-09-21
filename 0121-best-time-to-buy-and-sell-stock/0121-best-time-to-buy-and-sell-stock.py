class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit = 0
        # for i in range(len(prices)):
        #     curProfit = 0
        #     left = i
        #     right = i + 1
        #     while right < len(prices):
        #         curProfit = prices[right] - prices[left]
        #         maxProfit = max(maxProfit, curProfit)
        #         right += 1
        # return maxProfit 
        maxProfit = 0
        left = 0
        right = left + 1
        while right < len(prices):
            print(left,right)
            curProfit = prices[right] - prices[left]
            print(curProfit)
            maxProfit = max(maxProfit, curProfit)
            if prices[left] > prices[right]:
                left = right 
                right += 1
            else:
                right += 1
        return maxProfit
            