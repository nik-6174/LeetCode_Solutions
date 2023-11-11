# Title: 240. Search a 2D Matrix II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/search-a-2d-matrix-ii/description/


## Complexity O(n+m)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not (matrix[0][0] <= target <= matrix[-1][-1]):
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1  # Starting from the top-right corner

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # Move left in the current row if the value is too large
            else:
                row += 1  # Move down to the next row if the value is too small

        return False

# Complexity O(n log m)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not (matrix[0][0] <= target <= matrix[-1][-1]):
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Binary search function within a row
        def binary_search_row(row_num, target):
            left, right = 0, cols - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[row_num][mid] == target:
                    return True
                elif matrix[row_num][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        # Binary search on each row
        for row in range(rows):
            if matrix[row][0] <= target <= matrix[row][-1]:
                if binary_search_row(row, target):
                    return True
        return False
