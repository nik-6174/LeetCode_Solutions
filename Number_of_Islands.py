# Title: 200. Number of Islands
# Difficulty: Medium
# Problem: https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def flip(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0"
                flip(i+1, j)
                flip(i, j+1)
                flip(i-1, j)
                flip(i, j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    flip(i, j)
                    count += 1
        
        return count
