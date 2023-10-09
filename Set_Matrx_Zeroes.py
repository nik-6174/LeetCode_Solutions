# Title: 73. Set Matrix Zeroes
# Difficulty: Medium
# Problem: https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited_rows = set()
        visited_columns = set()
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    visited_rows.add(i)
                    visited_columns.add(j)
        
        for row in visited_rows:
            matrix[row] = [0] * m
        
        for column in visited_columns:
            for i in range(n):
                matrix[i][column] = 0
