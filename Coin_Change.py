# Title: 322. Coin Change
# Difficulty: Medium
# Problem: https://leetcode.com/problems/coin-change/description/

## Using dp

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp with infinity for all amounts
        dp = {i: math.inf for i in range(amount + 1)}
        # The number of coins needed for 0 amount is 0
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != math.inf else -1

