class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low, sell high
        #if continuosly downward trend dont buy
        #if see a upward trend, buy then sell it
        #profit only appears when there is an increase 

        profit = 0
        for i in range(1, len(prices)): 
        #we will compare the current with the previous price, bc index 0 has nothing before it so we start at index 1
            if prices[i] > prices[i-1]:
            #at this point, an increase happens (5>3, 5-3=2) so we have profit
                profit += (prices[i] - prices[i-1])
        return profit

