# Title: 329. Longest Increasing Path in a Matrix
# Difficulty: Hard
# Problem: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.max_length, n, m = 0, len(matrix), len(matrix[0])

        dp = [[0] * m for _ in range(n)]
        
        # define dfs
        def dfs(i, j, prev_val):
            if 0 <= i < n and 0 <= j < m and matrix[i][j] > prev_val:
                if dp[i][j]:
                    return dp[i][j]
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i+1, j, val),
                    dfs(i, j+1, val),
                    dfs(i-1, j, val),
                    dfs(i, j-1, val)
                )
                return dp[i][j]
            else:
                return 0
        
        # find the maximum path length starting from each position
        for i in range(n):
            for j in range(m):
                self.max_length = max(self.max_length, dfs(i, j, -1))
        
        return self.max_length
