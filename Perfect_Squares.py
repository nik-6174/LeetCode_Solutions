# Title: 279. Perfect Squares
# Difficulty: Medium
# Problem: https://leetcode.com/problems/perfect-squares/description

# using DP
class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize the DP array to store results for each number from 1 to n
        dp = [0] + [float('inf')] * n
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]

  # Using Queues ( More Efficient )
  from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        # Create a list of squares up to sqrt(n)
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        
        # Initialize a queue with the initial number n and level 0
        queue = deque([(n, 0)])
        
        # Initialize a set to keep track of visited numbers
        visited = set()
        
        while queue:
            num, level = queue.popleft()
            if num == 0:
                return level
            
            for square in squares:
                if num < square:
                    break
                if num - square not in visited:
                    visited.add(num - square)
                    queue.append((num - square, level + 1))

# Using Maths ( Most Efficient )

class Solution:
    def isSquare(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq*sq == n
        
    def numSquares(self, n: int) -> int:
        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2      # reducing the 4^k factor from number
        if (n & 7) == 7: # mod 8
            return 4

        if self.isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        for i in range(1, int(n**(0.5)) + 1):
            if self.isSquare(n - i*i):
                return 2
        # bottom case from the three-square theorem
        return 3

        
