# Title: 2482. Difference Between Ones and Zeros in Row and Column
# Difficulty: Medium
# Problem: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        counter = defaultdict(int)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    counter[i] -= 1
                    counter[-j-1] -= 1
                else:
                    counter[i] += 1
                    counter[-j-1] += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = counter[i] + counter[-j-1]
        
        return grid
