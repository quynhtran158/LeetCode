from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP array to store the minimum number of coins for each amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins to make amount 0
        
        # Update the dp array for each coin
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still infinity, it means it's impossible to make that amount
        return dp[amount] if dp[amount] != float('inf') else -1

        