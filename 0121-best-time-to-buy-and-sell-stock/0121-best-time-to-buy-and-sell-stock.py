class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low, sell high
        buy = float("inf")
        profit = 0

        for price in prices:
            if price < buy:
                buy = price #if the price decrease, then the profit will always be 0, since there is no update of sell
            else:  #price >= buy:
                profit = max(profit, price - buy)
        return profit  

        #set the first day as a buy
        # for i in range(len(prices)):
        #     if i == 0:
        #         buy = prices[i]
        #     elif prices[i] <= buy:
        #         buy = prices[i]
        #     elif prices[i] > buy:
        #         profit = max(profit,prices[i] - buy)
        #     else:
        #         return 0
        # return profit
    
    