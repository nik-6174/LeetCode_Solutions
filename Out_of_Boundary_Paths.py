# Title: 576. Out of Boundary Paths
# Difficulty: Medium
# Problem: https://leetcode.com/problems/out-of-boundary-paths/description

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @lru_cache(None)
        def dfs(i, j, k):
            if k < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            total = 0
            for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                total += dfs(x, y, k-1)
            return total % (10**9 + 7)

        return dfs(startRow, startColumn, maxMove)
