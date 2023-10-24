# Title: 289. Game of Life
# Difficulty: Medium
# Problem: https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        res = [[0] * m for _ in range(n)]

        def fill_edges(i: int, j: int) -> None:
            if i > 0:
                res[i-1][j] += 1
                if j > 0:
                    res[i-1][j-1] += 1
                if j < m - 1:
                    res[i-1][j+1] += 1
            if j > 0:
                res[i][j-1] += 1
                if i < n - 1:
                    res[i+1][j-1] += 1      
            if i < n - 1:
                res[i+1][j] += 1
                if j < m - 1:
                    res[i+1][j+1] += 1
            if j < m - 1:
                res[i][j+1] += 1
        
        def fill_not_edges(i: int, j: int) -> None:
            res[i-1][j] += 1
            res[i-1][j-1] += 1
            res[i-1][j+1] += 1
            res[i][j-1] += 1
            res[i+1][j-1] += 1
            res[i+1][j] += 1
            res[i+1][j+1] += 1
            res[i][j+1] += 1

        
        # fill res to find count of the alive neighbours for each cell
        for i in range(n):
            for j in range(m):
                if board[i][j]:
                    if i == 0 or i == n-1 or j == 0 or j == m-1:
                        fill_edges(i, j)
                    else:
                        fill_not_edges(i, j)
        
        # Update board according to the description
        for i in range(n):
            for j in range(m):
                if board[i][j]:
                    if not (2 <= res[i][j] <= 3):
                        board[i][j] = 0
                elif res[i][j] == 3:
                    board[i][j] = 1
