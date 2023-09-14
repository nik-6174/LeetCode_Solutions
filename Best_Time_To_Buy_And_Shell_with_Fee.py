# Title: 714. Best Time to Buy and Sell Stock with Transaction Fee
# Difficulty: Medium
# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

## Using DP
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        # Create two DP arrays to store the maximum profit with and without holding a stock on each day
        hold = [0] * n  # Maximum profit when holding a stock
        not_hold = [0] * n  # Maximum profit when not holding a stock
        
        # Initialize the first day
        hold[0] = -prices[0]  # Buying on the first day
        not_hold[0] = 0  # Not buying on the first day
        
        for i in range(1, n):
            # Update the DP arrays
            hold[i] = max(hold[i - 1], not_hold[i - 1] - prices[i])  # Either continue holding or buy on this day
            not_hold[i] = max(not_hold[i - 1], hold[i - 1] + prices[i] - fee)  # Either continue not holding or sell on this day
            
        return not_hold[n - 1]  # Return the maximum profit when not holding a stock on the last day


## More efficient solution
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        total = 0
        minimum = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                total += prices[i] - minimum - fee
                minimum = prices[i] - fee
        return total

## More efficient Solutions
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, profit = -prices[0], 0
        for i in range(1, len(prices)):
            buy = max(buy, profit - prices[i])
            profit = max(profit, buy + prices[i] - fee)
        return profit
            
