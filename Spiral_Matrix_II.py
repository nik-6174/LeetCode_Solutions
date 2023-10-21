# Title: 59. Spiral Matrix II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/spiral-matrix-ii/description/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        row, col, dr = 0, 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(1, n**2 + 1):
            matrix[row][col] = i
            next_row, next_col = row + directions[dr][0], col + directions[dr][1]

            if (
                next_row < 0
                or next_row >= n
                or next_col < 0
                or next_col >= n
                or matrix[next_row][next_col] != 0
            ):
                # Change direction if the next cell is out of bounds or already visited.
                dr = (dr + 1) % 4

            row, col = row + directions[dr][0], col + directions[dr][1]

        return matrix
