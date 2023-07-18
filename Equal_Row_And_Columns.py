# Title: 2352. Equal Row and Column Pairs (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

# Solution using defaultdict and tuples (Most efficient)
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # create a defaultdict with default value as 0
        d = defaultdict(int)
        # add the tuple for each row in the grid
        for row in grid:
            d[tuple(row)] += 1
        count = 0
        # create the column tuples
        for column in zip(*grid):
            count += d[column] # add the number of occurances of each row in columns
        return count

# Solution using tuples
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = [tuple(row) for row in grid]
        columns = []
        for j in range(len(grid[0])):
            columns.append(tuple([grid[i][j] for i in range(len(grid))]))
        count = 0
        for row in rows:
            count += columns.count(row)
        return count

# Solution using strings
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # create a list of string of row elements
        rows = [""]*len(grid)
        # create a list of string of columns elements
        columns = [""]*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # add the char in the ith row
                rows[i] += str(grid[i][j]) + ','
                # add the char in the jth column
                columns[j] += str(grid[i][j]) + ','
        count = 0
        # count the number of column strings in rows and columns
        for row in rows:
            count += columns.count(row)

        # return the number of equal row column pairs
        return count
        
