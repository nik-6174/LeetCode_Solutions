# Title: 130. Surrounded Regions
# Difficulty: Medium
# Problem: https://leetcode.com/problems/surrounded-regions/description

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != 'O':
                return
            board[i][j] = 'T'  # Mark it temporarily

            for x, y in directions:
                dfs(i + x, j + y)

        # Mark 'O's that are not surrounded by 'X' as 'T'
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and board[i][j] == 'O':
                    dfs(i, j)

        # Flip marked 'O's to 'X's and revert 'T's back to 'O'
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
