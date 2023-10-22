# Title: 790. Domino and Tromino Tiling
# Difficulty: Medium
# Problem: https://leetcode.com/problems/domino-and-tromino-tiling/description/

class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n
        MOD = 10**9 + 7

        # Create a DP array to store the number of ways to tile a 2 x i board
        dp = [0] * (n + 1)
        
        # Initialize the base cases
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            # You can place a 2 x 1 domino vertically or horizontally
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]
            
